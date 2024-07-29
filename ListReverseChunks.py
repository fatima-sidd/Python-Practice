sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

length = len(sample_list)

dividedLength = int(length/3)

for i in range(0,length, dividedLength):

    chunk = sample_list[i:i+dividedLength]
    print("Chunk: ", chunk)

    revChunk = chunk[::-1]
    print("Reversed Chunk: ", revChunk)

