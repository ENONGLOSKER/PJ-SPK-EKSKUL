import asyncio

async def fetch_data():
    print("Memulai pengambilan data...")
    await asyncio.sleep(2)  # simulasi operasi I/O yang memakan waktu
    print("Data berhasil diambil!")
    return {"data": "contoh_data"}

async def main():
    print("Mulai program")
    data = await fetch_data()  # tunggu hingga fetch_data selesai
    print(data)
    print("Selesai program")

# Menjalankan loop event
asyncio.run(main())
