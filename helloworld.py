from gensim.summarization import keywords

text = '''"Alert Today , Alive Tomorrow"

 Road Safety 🛣️is the biggest matter of concern to our country in this recent times. Various measures and awareness programs are implemented to make people aware of the gravity of this topic.
 
"It is the duty of each one of us to join in hands with the government in this issue to make our roads safe."

The Government considers the 18th of January to  17th February as the National Road Safety Month with the theme of year 2021 as "Sadak suraksha- jeevan Raksha" to spread the importance of road safety among the general public.

NSS MBCET UNIT 230  is immensely proud and happy to  organize an intercollege_ Slogan Writing Competition ✍️.
Details

▪️ Road Safety
▪️ Competition: Slogan writing
▪️ Date & Time: 13th  Feb 9 am - 14th Feb 9am 


Link to participate🔗
https://forms.gle/1QquWxPm6M13XVNr9

The winner  is entitled to receive an e-certificate 📜

Any queries❓
Contact📱
Vasundaraa:80782 62247
Aswen: 98467 23561'''

chumma = 1

print(keywords(text).split('\n'))