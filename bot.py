import openai

openai.api_key = "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"


def edit(text, instruction):
    response = openai.Edit.create(
        model="text-davinci-edit-001",
        input=text,
        instruction=instruction,
        temperature=0.9,
        top_p=1
    )

    return response
