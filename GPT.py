import openai
openai.api_key = "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"
prompt = "ChatGPT, can you please describe a new and innovative business idea that has the potential to be successful " \
         "in today's market? Please provide a detailed description of the idea. Your " \
         "answer should be structured as following: Idea, Problem, Target Audience \\n\\n after each." \
         "Revenue Model. But make sure your answer is no longer than 1024 characters. After your answer write a " \
         "prompt that will allow to google search an image fitting to the idea you described starting with " \
         "\"Prompt:\". The prompt should consist of two words and it should have some relation to the idea. "
def get_idea():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": prompt}
        ]
    )

    response = response.choices[0].message.content
    specific_word = "Idea:"
    #print(response.split(specific_word, 1))
    result = response.split(specific_word, 1)
   # print(result)
    response = specific_word + result[1 if len(result) > 1 else 0]
    with open("file.txt","w") as f:
        f.write(response)

    specific_word = "Prompt:"
    result = response.split(specific_word, 1)
    response = result[0]
    promp = result[1]

    return(response, promp)


#get_idea()