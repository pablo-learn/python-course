import asyncio

async def tarea(nombre):
    print(f"Hola {nombre}")

async def main():
    await asyncio.gather(
        tarea("Ana"),
        tarea("Bob")
    )

asyncio.run(main())