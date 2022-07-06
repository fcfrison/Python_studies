import asyncio

def main():
    print("inicia função")
    async def faz_algo():
        print("Fazendo alguma coisa")
    task = asyncio.ensure_future(faz_algo())
    asyncio.run(task)
    
    print("fim")

if __name__=='__main__':
    main()