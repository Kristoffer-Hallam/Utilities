import qrcode

meu_qrcode = qrcode.make(
    "https://realpython.com/"
)

meu_qrcode.save("qrcode.png")
# meu_qrcode.show()