import streamlit as st
import random 
preguntas = {
    1: {"question": "is salt good for you?", "answers": ["yes","no","dosed"], "answer":2, "justicication": "sodium (salt) is important in small quantities because can regulate the blood presure, that's why hypertension can be caused by too much salt."},
    2: {"question": "should you take caffeine if you have a heart desease?", "answers": ["yes","no","dosed"], "answer":1, "justification": "caffeine makes the heart to go faster and for a heart desease that can end at a tachycardia."},
    3: {"question": "how much times a week should you aim for moderate-intense exercise?", "answers": ["never","2-times a week","once a week", "5 times a week"], "answer":3, "justification":"exercice must be done as much as possible to take away bad choresterol and fat"},
    4: {"question": "which of this factors can be modified to avoid a heart desease?", "answers": ["drug addiction","genetics","family traits"], "answer":0, "justification": "drug addiction is an adiction to intoxicate the body with substances from outside."},
    5: {"question": "which of the following habits is bad for the heart?", "answers": ["exercising","eating","smoking"], "answer":2, "justification": "drug addiction as smoking an adiction to intoxicate the body with substances from outside."},
    6: {"question": "is stress good for the heart?", "answers": ["yes","no"], "answer":1, "justification": "emotional states can influenze health."},
    7: {"question":"what role the good choresterol(LDL) plays on our body?", "answers":["to  bock the veins", "avoid bad choresterol to block the veins"], "justification":"they are called triglicerids and avoid blood contamination with the bad choresterol(HDL)."},
    8: {"question": "why should you make exercise?", "answers": ["health","fasion","esthetic"], "answer":0, "justification": "health and life is more important than fashion or estethic"},
    9: {"question": "does alcohol leads to heart damage?", "answers": ["yes","no"], "answer":0, "justification": "alcohol intoxication is bad for blood."},
    10: {"question": "should you consume psicoactive substances?", "answers": ["yes, of course","no, nobody should do it","no, with exeption of a psiquiatric desease"], "answer":2, "justification": "psicoactive substances are bad for the heart, but if a psiquiatrist tells you to take them you must."},
    11: {"question": "which one is healthy and you should consume more than the others?", "answers": ["burger","hot dog","salad", "fries"], "answer ":2, "justification": "salad is the healthiest because doesn't has choresterol."},
    12: {"question": "which activity should you do daily?", "answers": ["smoke","eat ice cream","exercising"], "answer":2, "justification": "exercising burns fat and avoids bad choresterol(HDL) for blocking the veins."},
    13: {"question": "which of the following foods is damageful for the heart?", "answers": ["meat","donuts","vegetables"], "answer":1, "justification": "donuts are rich in fats and bad choresterol (HDL)."},
    14: {"question":"which of the following can cause a heart desease?", "answers":["smoking cigarette", "eating salad", "exercising"], "answer":0, "justification": "cigarette is fatal for the hart because diminuts good choresterol(HDL)"},
    15: {"question": "which of the following can lead to hypertension?", "answers": ["vitamins","proteins","salts"], "answer":2, "justification": "salts increase blood presure so they help to control blood presure and exces can lead to hypertension."},
    16: {"question": "what is sedentarism?", "answers": ["excess movement","missing salt","hyper activity", "missing exercise"], "answer":3, "justification":"missing exercise can contribute heart desseases and is callled sedentarism."},
    17: {"question": "caffeine:", "answers": ["increases sugar","increases hert rate","decreases anxiety"], "answer":1, "justification": "cafeine accelerates heart rate and inhibits adenosine, that relaxes your body and your brain."},
    18: {"question": "the heart's function is:", "answers": ["analyses information from senses","pumps blood through the body","processes fats and makes hormones"], "answer":1, "justification": "the heart pumps blood and without that we couldn't live, that's why is important to take care of it"},
    19: {"question": "increased blood tension is called", "answers": ["hypertension","hyperthrophy","diabetes"], "answer":0, "justification":"hypertension is increased blood presure that can be the cause of many cardiovascular deseases and can be caused by excess salt in food and many other factors."},
    20: {"question": "why is important to take care of the heart?", "answers": ["to have a healthier life and live more time", "think better and looking better", "to be race winner"], "answer": 0, "justification": "the heart keeps us alive."},
    21: {"question": "________ is a controlable risk factor for avoiding heart deseases.", "answers": ["genetics", "food", "family"], "answer":1, "justification":"food can be modified with diet"},
    22: {"question": "how is heart affected by hormones?", "answers": ["through air", "through water", "through blood"], "answer":2, "justification": "hormones travel through blood"},
    23: {"question": "is choresterol good?", "answers":["yes", "no", "HDL", "LDL"], "answer":3, "justification": "LDL avoids HDL to acumulate in the veins."},
    24: {"question": "which of the following diet is more recomended for the heart?", "answers": ["fast food diet", "BBQ diet", "mediterrean diet"], "answer":2, "justification": "mediterrean diet is rich in what is called good fats "},
    25: {"question": "Jade goes to school running and when she gets home she eats pasta and tomato and lettuce salad, but Tim gets to school by car and he eats a burger when he gets home. Who is healthier?", "answers":["Jade", "Tim", "none"], "answer":0, "justification": "jade's habits are healthier for example when she goes to school by running she makes exercise and pasta is rich in proteins and good fats."},
    26: {"question": "adrenaline _______", "answers":["makes you sad", "stops heart beat", "makes you afraid and increases heart beat"], "answer":2, "justification": "that's adrenaline's funtions at nature."},
    27: {"question": "________ is the scientific name for sugar.", "answers":["metabolites", "enzymes", "carbohydrates"], "answer":2, "justification": "sugars as glucose or sacarose are called carbohydrates."},  
    28: {"question": "meat is ________ for the heart.", "answers":["good", "bad", "no diference"], "answer":0, "justification": "some studies have shown that proteins in meat are good for the heart."},
    29: {"question": "is sugar linked to heart deseases?", "answers":["yes", "no", "is not linked"], "answer":0, "justification": "excess sugar can cause diabetesthat is linked with heart deseases."},
    30: {"question": "which is ad for the heart", "answers": ["simple carbohydrates", "complex carbohydrates", "all from above"], "answer":0, "justification": "simple carbohydrates are the bad sugars that can lead to diabetes which is linked to heart deseases."},
    31: {"question": "good choresterol is", "answers":["all", "LDL", "HDL"], "answer":1, "justification": "that's how good choresterol is called."},
    32: {"question": "which of the following kinds of meat is bad for the heart?", "answers":["beef", "pork", "sausage"], "answer":2, "justification": "sausage is rich in bad choresterol (HDL) so increases the risk of blocking coronary veins"},
    33: {"question": "which of the folowing can block the veins and can increase the risk of a heart attack?", "answers":["meat", "steroids", "water"], "answer":1, "justification": "steroids are based on choresterol and almost always on HDL or the bad one so blocks the coronary arteries."},
    34: {"question": "salt _____ blood pressure", "answers": ["raises", "decreases", "makes  it to stay the same"], "answer":0, "justification": "salt (sodium) raises blood pressure and the right quantiti msakes blood presure stable."},
    35: {"question": "which of the following is a cardiovascular desease?", "answers": ["choresterol", "auricular fibrilation", "diabetes"], "answer":1 , "justification": "a cardiovascular desease is a desease in the heart, arteries or both."},
    36: {"question": "can stress affect your cardiovascular health", "answers": ["yes", "no"], "answer":0 , "justification": "stresse's hormone can negatively affect heart health"},
    37: {"question": "are hormones related to heart health?", "answers": ["yes", "no"], "answer":0 , "justification": "hormones affect each cell in the body"},
    38: {"question": "neame the 2 ways steroids can affect your health", "answers": [" hormones and water", "blood presure and sugar", "choresterol and hormones"], "answer":2 , "justification": "steroids have a hormone activator based on choresterol"},
    39: {"question": "the hormone of stress is", "answers": ["melatonine", "cortisol", "dopamine"], "answer":1 , "justification": "the hormines can affect your emotion such as dopamine for hapyness and for stress cortisol"},
    40: {"question": "the minimum heart rate is", "answers": ["120bpm", "40bpm", "60bpm"], "answer":2 , "justification": "doctors noticed that a healthy heart rate depends on you but the minimum is 60bpm"},
    41: {"question": "How does smoking affect the heart?", "answers": ["hormones", "choresterol", "directly"], "answer":1 , "justification": "choresterol based product are found in cigarete that get into the blood with oxygen and can cause several damage to the heart and other organs."},
    42: {"question": "How does air pollution affect heart health?", "answers": ["by blood", "by hormones", "by mind"], "answer":0 , "justification": "chemicals get to the heart by blood."},
    43: {"question": "heart deseases can cause:", "answers": ["stomach problems", "mental problems", "epilepse"], "answer":2 , "justification": "epilepse can be caused by heart broblems related to sugar and tension and can break blood vessels in the brain and that can lead to seizures."},
    44: {"question": "william and Sasha are brothers and they're going for lunch, Shara says she wants a roast beef with a burger and fries, but William says he thinks is better to have a meat, then a salad and rice. Who is takin care of it's heart?", "answers": ["none", "Shara", "William"], "answer":2 , "justification": "williams purposal has less saturated fats and less choresterol so is healthier."}
    }
global score
score = 0
nq = 10

for e in range (nq):
    apreg = random.choice(list(preguntas.keys()))
    radio = preguntas[apreg]["answers"]
    ans = preguntas[apreg]["answer"]
    u_answer = st.radio("answer here:", radio, key=e+5)
    quest = preguntas[apreg]["question"]
    if st.button("check", key=f"this is the buttons key {e+17}"):
         if "answer" in preguntas[apreg]:
            st.title("think in heart")
            st.write(quest)
            u_answer
            def result(u_answer, ans):
                if radio.index(u_answer) == ans:
                    return "c"
                else:
                    return "i"
            reslt = result(u_answer, ans)
            if reslt == "c":
                st.success("great you did it!")
                st.write(preguntas[apreg]["justification"])
                score += 5
            else:
                st.error("sorry, keep trying")
                st.write(F"the answer was {ans}")
                score -= 1
                st.write(preguntas[apreg]["justification"])
                st.write(f"your score is {score} from this lesson")