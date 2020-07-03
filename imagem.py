from PIL import Image

track = Image.open("car_track2.jpg", 'r')
vet = []
for i in track:
    if i not in vet:
        vet.append(i)

track.close()
print(vet)
