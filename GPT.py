import openai
openai.api_key = "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"
prompt = "ChatGPT, can you please describe a new and innovative business idea that has the potential to be successful " \
         "in today's market? Please provide a detailed description of the idea, including the problem it solves, " \
         "the target audience, the unique selling proposition, and the revenue model. Additionally, please provide " \
         "any insights on the market and consumer behavior that may be relevant to the success of this idea. Your " \
         "answer should be structured as following: Idea, Problem, Target Audience, Unique Selling Proposition, " \
         "Revenue Model, Insights on the Market and Consumer Behavior, Conclusion. "
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
    print(response.split(specific_word, 1))
    result = response.split(specific_word, 1)
    print(result)
    response = specific_word + result[1 if len(result) > 1 else 0]
    with open("file.txt","w") as f:
        f.write(response)
    return(response)


