import asyncio

async def tarea(nombre):
    print(f"Hola {nombre}")

async def main():
    await asyncio.gather(
        tarea("Ana"),
        tarea("Bob")
    )
    await tarea("Carlos common await")

asyncio.run(main())