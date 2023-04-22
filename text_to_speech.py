# Import the required modules
from gtts import gTTS
import os


# let's create a function
def text_to_speech(text, language, filename=None, play=True):
    # Create an gTTS instance
    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    obj = gTTS(text=text, lang=language, slow=False)
    # Save the converted audio
    obj.save(savefile=f"{filename}.mp3")
    # Playing the converted audio file
    if play:
        os.system(f"{filename}.mp3")
        exit()


if __name__ == '__main__':
    # text = """Machine learning is a branch of artificial intelligence that involves the use of algorithms and statistical models to enable computer systems to improve their performance on a specific task without being explicitly programmed. The algorithms used in machine learning are designed to identify patterns in data and make predictions or decisions based on those patterns. Machine learning has a wide range of applications, from image recognition and speech recognition to fraud detection and personalized marketing. As more and more data is generated and collected, machine learning is becoming increasingly important in helping businesses and organizations make sense of this data and gain valuable insights that can drive innovation and growth."""
    text = """মেশিন লার্নিং হলো একটি কৃত্রিম বুদ্ধিমত্তা শাখা, যা সংখ্যা মডেল এবং অ্যালগরিদমগুলি ব্যবহার করে কম্পিউটার সিস্টেমগুলির কাজকর্ম সহজ করে। এই এলগরিদমগুলি এক্সপ্লিসিটলি প্রোগ্রামিং না করে ডেটা প্যাটার্ন আনতে এবং সেগুলি ভিজ্যুয়ালাইজ করে নিয়ম তৈরি করে কাজ করে। মেশিন লার্নিং এর ব্যবহার আইটি সেক্টরের প্রায় সব ক্ষেত্রে সম্ভব, যেমন চিত্র এবং ভোকাল পরিচিতি করা, ফ্রড ডিটেকশন এবং ব্যক্তিগতকৃত বিপণন। আরো ডেটা সংগ্রহ এবং একত্রিত হওয়া যায় তার মাধ্যমে মেশিন লার্নিং বিশ্বে দ্রুত ছড়িয়ে উঠছে এবং ব্যবসার জন্য অনেক গুরুত্বপূর্ণ ইনসাইট উপস্থাপন করে।"""
    text_to_speech(text=text, language='bn', filename="myaudio")
    print("Execution completed")
