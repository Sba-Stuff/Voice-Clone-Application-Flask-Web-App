# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import *
import sys
import os
from werkzeug import secure_filename

#TEMPLATE_DIR = os.path.abspath('../templates')
#STATIC_DIR = os.path.abspath('../static')
# app = Flask(__name__) # to make the app run without any
#app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = {"wav","mp3"}
app = Flask(__name__,template_folder="template/",static_folder="static/")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#@app.route('/output/<path:filepath>')
#def stater(filepath):
#    return send_from_directory('output', filepath)

@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

def htmloader(text,inputaudio,outputaudio):
    x = ""
    x+="Utterance: <p>"+text+"</p><br>"
    x+="Original:<br>"
    x+="<audio controls>"
    x+="  <source src='"+inputaudio+"' type='audio/"+inputaudio.rsplit('.', 1)[1].lower()+"'>"
    x+="</audio><br>"
    x+="Cloned Utterance:<br>"
    x+="<audio controls>"
    x+="  <source src='"+str(outputaudio)+"' type='audio/wav'>"
    x+="</audio><br>"
    return x

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def upload_file():
    fil = []
    if request.method == 'POST':
        f = request.files['file']
        if allowed_file(f.filename):
            f.save(UPLOAD_FOLDER+secure_filename(f.filename))
            fil.append("File uploaded successfully")
            fil.append(UPLOAD_FOLDER+secure_filename(f.filename))
            return fil
        else:
            fil.append("Not An Expected File")
            return fil
@app.route('/',methods=['GET', 'POST'])
def hello_world():
    legoutput = upload_file()
    lig = "This is a demo utterance. This will work when you do not add any utterance."
    if request.method == 'POST':
        lig = request.form["textarea"]
    print(str(lig))
    #return mainpage()
    if str(legoutput)=="None":
        return render_template("index.html",output="")
    else:
        from encoder.params_model import model_embedding_size as speaker_embedding_size
        from utils.argutils import print_args
        from synthesizer.inference import Synthesizer
        from encoder import inference as encoder
        from vocoder import inference as vocoder
        from pathlib import Path
        import numpy as np
        import librosa
        import argparse
        import torch
        try:
            parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
            parser.add_argument("-e", "--enc_model_fpath", type=Path,default="encoder/saved_models/pretrained.pt")
            parser.add_argument("-s", "--syn_model_dir", type=Path,default="synthesizer/saved_models/logs-pretrained/")
            parser.add_argument("-v", "--voc_model_fpath", type=Path,default="vocoder/saved_models/pretrained/pretrained.pt")
            parser.add_argument("--low_mem", action="store_true")
            #parser.add_argument("--no_sound", action="store_true")
            args = parser.parse_args()
            print_args(args, parser)
            #if not args.no_sound:
            #    import sounddevice as sd
            encoder.load_model(args.enc_model_fpath)
            synthesizer = Synthesizer(args.syn_model_dir.joinpath("taco_pretrained"), low_mem=args.low_mem)
            vocoder.load_model(args.voc_model_fpath)
            num_generated = 0
            in_fpath = legoutput[1]
            print(str(in_fpath))
            preprocessed_wav = encoder.preprocess_wav(in_fpath)
            original_wav, sampling_rate = librosa.load(in_fpath)
            preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)
            embed = encoder.embed_utterance(preprocessed_wav)
            print("Created the embedding")
            text = str(lig)
            texts = [text]
            embeds = [embed]
            specs = synthesizer.synthesize_spectrograms(texts, embeds)
            spec = specs[0]
            print("Created the mel spectrogram")
            print("Synthesizing the waveform:")
            generated_wav = vocoder.infer_waveform(spec)
            generated_wav = np.pad(generated_wav, (0, synthesizer.sample_rate), mode="constant")
            #if not args.no_sound:
            #    sd.stop()
            #    sd.play(generated_wav, synthesizer.sample_rate)
            fpath = "static/output.wav"
            print(generated_wav.dtype)
            librosa.output.write_wav(fpath, generated_wav.astype(np.float32),synthesizer.sample_rate)
            print("\nSaved output as %s\n\n" % fpath)
            return render_template("index.html",output=htmloader(text,legoutput[1],fpath))
        except Exception as e:
            return render_template("index.html",output="Caught exception: %s" % repr(e))
    #return xieon
# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()