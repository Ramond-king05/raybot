from flask import Flask,request
import requests
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)
@app.route('/',methods=['POST'])

def bot():
    user_msg=request.values.get('Body','').lower()
    bot_resp=MessagingResponse()
    msg=bot_resp.message()
    
    
    if 'hello' in user_msg:
        msg.body("Hi there!, I AM RAMOND'S  AI BOT" )


    elif 'what can you do' in user_msg:
        msg.body('i can teach you the wonderful steps in making a delicious puff puff')
    
    elif 'good morning' in user_msg:
        msg.body('Morning,I trust you had a wonderful night rest')
    
    
    elif 'yes' in user_msg:
        msg.body("wow,that's so amazing!")
    
    
    elif 'good afternoon' in user_msg:
        msg.body('afternoon,how has your day been')
    
    
    elif 'fine' in user_msg:
        msg.body('Glad to hear that')
    
    
    elif 'thank you' in user_msg:
        msg.body('You are always welcome')
    
    
    elif 'who is the coach of the person who developed you' in user_msg:
        msg.body('my developer coah is Almighty sir Ruben')     
    
    
    elif 'who created you' in user_msg:
        msg.body('I was created by Fasasi Abdul-Rahman Temitope (Ramond king)')
    
    
    elif 'wow' in user_msg:
        msg.body('i can see that you are impressed, you can just call my creator on this line +2349017152461')    
    
    
    elif 'yeah' in user_msg:
        msg.body(' Want to know about Python? Just type the word Python')
    
    
    elif 'python' in user_msg:
        msg.body('Python is a high-level, interpreted, interactive and object-oriented scripting programming language python is designed to be highly readable It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.')
    
    
    elif 'what do you have for me' in user_msg:
        msg.body("want some quote? type quote")
    
    
    elif 'quote' in user_msg:
        msg.body("ANY FOOL CAN WRITE CODE THAT COMPUTER UNDERSTAND, GREAT PROGRAMMERS WRITE CODE HUMANS UNDERSTAND.")        
    
    
    elif 'what is module' in user_msg:
        msg.body('A Module is a Python script that generally contains import statements, functions, classes and variable definitions, and Python runnable code and it “lives” file with a ‘.py’ extension zip files and DLL files can also be modules.Inside the module, you can refer to the module name as a string that is stored in the global variable name.')
    
    
    elif "that's nice" in user_msg:
        msg.body('Awwwwwwn thank you')

    #elif 'you are welcome':
    #    msg.body("alright.")    
    
    
    elif 'what can you teach me' in user_msg:
        msg.body('Want to know how to make puff puff? Just type the word puff puff')
    
    
    elif 'puff puff' in user_msg:
        msg.body(
            '''INGREDIENTS 
        3 cups all-purpose flour
        1 tablespoon instant yeast
        1/2 cup sugar
        1/4 cup powdered milk, optional
        1/4 teaspoon salt
        1/4 teaspoon grated nutmeg
        1/4 teaspoon cinnamon powder
        2 cups warm water
        Oil for deep frying
        TO COUNTINUE TYPE 'step 1'.
             
            ''')
    
    
    elif 'step 1' in user_msg:
        msg.body('''Step 1 :
    Add the dry ingredients except for the salt into a big bowl.
    
    TYPE 'step 2' TO CONTINUE''')
    
    
    elif 'step 2' in user_msg:
        msg.body('''Step 2 :
    Mix the dry ingredients, add the warm water and salt and mix until smooth and lump-free.
    
    TYPE 'step 3' TO CONTINUE''')
    
    
    elif 'step 3' in user_msg:
        msg.body('''Step 3 :
    Cover the bowl with plastic wrap and/or kitchen napkin and leave in a warm spot until doubled in bulk.
    
    TYPE 'step 4' TO CONTINUE''')
    
    
    elif 'step 4' in user_msg:
        msg.body('''Step 4 :
    About 40 minutes later…
    
    
    TYPE 'step 5' TO CONTINUE''')
    
    
    elif 'step 5' in user_msg:
        msg.body('''Step 5 :
    Deflate batter and give it a very good mix (pulling the dough towards you), then heat up some oil for deep frying
    
    
    TYPE 'step 6' TO CONTINUE''')
    
    
    elif 'step 6' in user_msg:
        msg.body('''Step 6 :
    You will notice the change in texture after about 5 minutes and it would continue to rise
    
    
    TYPE 'step 7' TO CONTINUE''')
    
    
    elif 'step 7' in user_msg:
        msg.body('''Step 7 :
    Test to make sure the oil is hot enough by dropping a teaspoon of batter into it. 
    If batter flows to the top then it’s fine.
    If it browns too quickly, oil is too hot, take off the heat and cool for a minute.
    Using a rounded tablespoon or your hand, drop batter into hot oil and fry till bottom is golden brown, turn balls over and fry till it’s golden brown all over.

    TYPE 'step 8' TO CONTINUE''')
    
    
    elif 'step 8' in user_msg:
        msg.body('''Step 8 :
    Using a slotted spoon, take out Puff Puff and place on paper napkins to soak up excess oil.
    Continue the process till you use up all the batter.
    
    TYPE 'step 9' TO CONTINUE''')
    
    
    elif 'step 9' in user_msg:
        msg.body('''Step 9 :
    Enjoy with your favourite drink.            
    
    TYPE 'conclusion' to see the sumarry of the steps stated''') 
    
    
    elif 'conclusion' in user_msg       :                                                                                                                                                                                                                                                                                                                                                              
        msg.body("It can be enjoyed at home,school or even big event parties. it can also be a strarting point of your busienss")


    

    elif 'quote' in user_msg:
        r=requests.get('https://api.quotable.io/ramdom')
        if r.status_code==200:
            data=r.json()
            quote=f'{data["content"]} ({data["author"]})'
        else:
            quote='I could not find any quote at the moment,sorry'
        msg.body(quote)
    
    elif 'cat' in user_msg:
        msg.media('https://cataas.com/cat')
    
    
    else:
        msg.body("I didn't get what you have said, You can call this number for further information +2349017152461" )
    return str(bot_resp)

    
     
if __name__ == '__main__':
    app.run(debug=True)           
       