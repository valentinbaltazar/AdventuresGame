"""Run audio model, and output voice over from text"""
import torch
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer
import soundfile as sf
import sounddevice as sd

class ParlerTTSGenerator:
    def __init__(self, model_name="parler-tts/parler-tts-mini-v1", device=None):
        self.device = device if device else ("cuda:0" if torch.cuda.is_available() else "cpu")
        self.model = ParlerTTSForConditionalGeneration.from_pretrained(model_name).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def generate_audio(self, prompt, description, output_file="parler_tts_out.wav", play_audio=False):
        input_ids = self.tokenizer(description, return_tensors="pt").input_ids.to(self.device)
        prompt_input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.device)
        
        generation = self.model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids)
        audio_arr = generation.cpu().numpy().squeeze()

        # Save the audio to a file
        sf.write(output_file, audio_arr, self.model.config.sampling_rate)

        # Play the audio if requested
        if play_audio:
            self.play_audio(audio_arr, self.model.config.sampling_rate)

        return output_file

    def play_audio(self, audio_data, sampling_rate):
        """Play the generated audio using sounddevice."""
        sd.play(audio_data, samplerate=sampling_rate)
        sd.wait()  # Wait until the audio finishes playing

if __name__ == '__main__':
    # Example usage:
    tts = ParlerTTSGenerator()
    tts.generate_audio(
        prompt="Hey Anaruth, how are you doing today? Do you want to play an adventure game?",
        description="A deep male speaker with moderate speed and pitch. The recording is of very high quality, with the speaker's voice sounding clear and very close up.",
        play_audio=True  # Set to True to play the audio after generation
)
