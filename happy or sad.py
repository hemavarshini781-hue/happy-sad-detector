def evalulate():
  def count_mood():
    train_data =[
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")]
    for words,sentence in enumerate(train_data):
        happy_score=0
        sad_score=0
        if(words=="Happy"):
          happy_score+=1
        else:
          sad_score+=1  
        return(happy_score,sad_score)
  def guess_mood(sentence):
    happy=0
    sad=0
    happy_words=["full marks","won","surprise","tasty","excited","selected","finally","favourite"]
    sad_words=["lost","failed","moving","cancelled","upset","missed","stopped","lonely"]
    happy_words=0
    sad_words=0
    if(sentence==happy_words):
      happy+=1
    else:
      sad+=1
  def pratice_tasks():
    moods=0
    practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")]
    moods+=guest_mood(pratice_data)
    total=5
    percentage=(moods/total)*100
    print(f"percentage=:.2f",percentage)
if __name__ == "___main__":
      evaluate()

  
