import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(
        content=f'<h3>Hello from fast api</H3>'
    ).send()