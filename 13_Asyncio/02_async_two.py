import asyncio

async def brew_chai():
    print("Brwing Chai...")
    await asyncio.sleep(2)
    print("Chai is ready")
    
asyncio.run(brew_chai())