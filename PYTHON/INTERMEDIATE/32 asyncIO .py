import asyncio
async def fun1():
    await asyncio.sleep(3)
    print("fun 1")
async def fun2():
    await asyncio.sleep(1)
    print("fun 2")
async def fun3():
    await asyncio.sleep(1)
    print("fun 3")
async def main():
    L=await asyncio.gather(
        fun1(),
        fun2(),
        fun3(),
    )
    print(L)
asyncio.run(main())