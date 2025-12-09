
define Jack = Character("Jack", color="#c8ffc8")
define dead = Character("deads")
define maid = Character("Lucy", color="#ffc8c8")
define gardener = Character("Mike", color="#c8c8ff")
define wife = Character("Anna", color="#ffffc8")
define cook = Character("Robert", color="#ffc8ff")



label start:

    #wife killed him

    scene bg office 

  
    show jack netural at left

    
    voice "audio/jack1.wav"
    Jack "Another case its almost like they never end.It's just me ,and that usually dosen't happen. We must be spread thin this time of year."

    voice "audio/jack2.wav"
    Jack"Rich guy appears to have been murdered in his own home. We have five people on the premises. The maid, the cook, the gardener, and the victim's wife." 
    
    voice "audio/jake3.wav"
    Jack"Time to get to work."

    scene bg death
    show jack netural at left
    show deads body at right

    voice "audio/jake4.wav"
    Jack "Based on what I can see and on the report. There is a knife wound stright into the neck. There is no sign of a struggle. So he most likely knew his killer and was caught by surprise." 

    voice "audio/jake5.wav"
    Jack " I have nothing other than the person who found the body the maid. She says she came into the room to clean up for the day and found him like this. I guess that is where I will have to start."

    scene bg intergation

    show jack netural at left
    show lucy netural at right

    voice "audio/Jake6.wav"
    Jack "Hello ma'am I'm Jack the lead detective on this case, please have a seat."

    voice "audio/maid1.wav"
    maid "Thank you detective."

    voice "audio/jake7.wav"
    Jack" So I have to read you rights before we start. Relax it is just standard procedure." 

    voice "audio/jake8.wav"
    Jack"You have the right to remain silent. Anything you say can and will be used against you in a court of law. You have the right to an attorney. If you cannot afford an attorney, one will be appointed for you. Do you understand these rights as I have read them to you?"

    voice "audio/maid2.wav"
    maid "Yes I understand."
    voice "audio/jack9.wav"
    Jack "Good. Now can you tell me what you were doing around the time you saw the body?"
    voice "audio/maid3.wav"
    maid "I was doing my usual cleaning rounds. I had just finished the kitchen and when I went to my boss's room that is when I saw his body."

    label maid_interaction:
        voice "audio/jack10.wav"
        Jack "What question do I want to ask"
    menu:
        
        "What time was it when you found the body?" :
            jump choices1_a
        
        "Did you notice anything unusual on that day?":
              jump choices1_b
    label choices1_a:
        voice "audio/maid4.wav"
        maid "If I remember correctly it was around 7 pm."
        jump choices1_common
    label choices1_b:
        voice "audio/maid5.wav"
        maid "There was two things that were unusual. First, the cook was not in the kitchen the whole time I was there and I heard agurment coming from the boss's room earlier in the day, but that is all."
        jump choices1_common
    label choices1_common:
        Jack "Is there any thing else that you want to tell me? That might help the case."
        maid "Yes, look into the gardener. I saw him hanging around the house more than usual that day."

        Jack "Thank you for your time ma'am. I will be in touch if I have any more questions."
        hide lucy netural
        label first_person:
        Jack"Who do I want to talk to next?"
        default gardener_chosen=False
        default wife_chosen=False
    menu:
        "The Gardener":
            jump gardener_interaction
        "The Wife":
            jump wife_interaction
    label choices3_common:
        if gardener_chosen==False:
            menu:
                "Gardener":
                    jump gardener_interaction 
        if wife_chosen==False: 
            menu:
                "Wife":
                    jump wife_interaction
        else:
            jump cook_interaction 
    label gardener_interaction:
        show mike netural at right 
        $ gardener_chosen=True
        Jack " Hello sir I'm Jack the lead detective on this case, please have a seat."

        gardener "Sure thing detective."

        Jack" So I have to read you rights before we start. Relax it is just standard procedure."

        Jack"You have the right to remain silent. Anything you say can and will be used against you in a court of law. You have the right to an attorney. If you cannot afford an attorney, one will be appointed for you. Do you understand these rights as I have read them to you?"

        gardener "Yes I understand."

        Jack "Good. Now can you tell me what happend around the time you saw the body?"

        gardener "I was done working for the day and was waiting for my ride home. Since my car broke down earlier that week."

        gardener "Then I heard a scream coming from the room of the boss. I ran over to see what was going on and that's when I saw the maid standing over the body."

        Jack "I see. Did you notice anything unusual that day?"

        gardener " Now that you mention it. I did hear an argument coming from the boss's room earlier that day."

        Jack "Who was arguing?"

        gardener "I couldn't really tell since I never got a clear view of who it was."

        Jack "Understood. Do you know what they were arguing about?"

        gardener "No I have no idea what."

        label gardener_accu:
            Jack "Should I confront him about the accusation from the maid?"
        menu:
            "Yes":
                jump gardener_accused
            "No":
                jump choices2_common

        label gardener_accused:
            Jack " Someone said that they saw you hanging around the house more than usual that day. Can you explain that?"
            
            gardener " Who said that!! It's like I already told you I was waiting for my ride home"

            Jack "Calm down sir. All am trying to do is my job, okay."
            jump choices2_common
        label choices2_common:

        Jack "Is there anything else that you want to tell me? That might help the case."

        gardener "No I don't think so."
        hide gardener netural 
        jump choices3_common

        hide mike netural
        label wife_interaction:
            show anna netural at right 
            $ wife_chosen= True
            Jack " Hello ma'am I'm Jack the lead detective on this case, please have a seat."

            wife "Thank you detective."

            Jack" So I have to read you rights before we start. Relax it is just standard procedure."

            Jack"You have the right to remain silent. Anything you say can and will be used against you in a court of law. You have the right to an attorney. If you cannot afford an attorney, one will be appointed for you. Do you understand these rights as I have read them to you?"

            wife "Yes I understand."

            Jack "Good. So can you tell me what you were doing around the time the body was found?"

            wife "I was with the cook disussing the meals for the upcoming party that we were hosting." 

            Jack "Where was this meeting taking place?"

            wife "In the kitchen."

            Jack " Okay. So you guys were discussing the menu heard a scream and came to see what was going on and saw that the maid found the body? Correct?"

            wife "Yes that is correct."

            Jack" Who was in the room when the body was found?"

            wife "The maid and the gardener were there."

            Jack "Did you hear anything unusual that day?"

            wife "No not that I can recall."

            Jack "Okay, is there anything else that you want to tell me? That might help the case."

            wife "No I don't think so."
            hide anna netural
            jump choices3_common

        label cook_interaction:
            show robert netural at right 
            hide anna netural
            hide mike netural 
            Jack " Hello sir I'm Jack the lead detective on this case, please have a seat."

            cook "Sure thing detective."#(In a worried tone)

            Jack" So I have to read you rights before we start. Relax it is just standard procedure."

            Jack"You have the right to remain silent. Anything you say can and will be used against you in a court of law. You have the right to an attorney. If you cannot afford an attorney, one will be appointed for you. Do you understand these rights as I have read them to you?"

            cook "Yes I understand." #(nervously)

            Jack" Are you okay man? You seem a bit on edge."

            cook " Yeah, am fine."

            Jack "Good. So can you tell me what you were doing around the time the body was found?"

            cook "I was in the kitchen with the wife disussing the meals for the upcoming party that we were hosting."

            Jack "Okay so you guys were discussing the menu heard a scream and came to see what was going on and saw that the maid found the body? Correct?"

            cook "Yes that is correct."

            Jack " You and the wife came into the room together? See the maid and the gardener there?"

            cook "Yes."

            Jack "Did you notice anything unusual that day?"

            cook " No not that I can recall."

            Jack" So there seems to be a little foil in what happened"

            Jack" You said you were in the kitchen with the wife when the body was found, bu the maid never saw you there."

            cook " I...I don't know what to say."

            Jack " Come on man, just be honest with me. You are not in any trouble "

            cook "Alright, alright. When the murder happened I went to go to the bathroom and that's when I heard them arguing. Then she came out covered in blood"
            
            Jack "The wife?"

            cook "Yes, she told me to be quite or I was next, so I complied "








    return
