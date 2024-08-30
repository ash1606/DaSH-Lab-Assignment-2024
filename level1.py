import json
import time
from groq import Groq

#--------------------------------
def make_object(str, line, time_sent, time_rcvd):
    prompt = line.strip('\n')
    obj = {
        "Prompt": prompt,
        "Message": str,
        "TimeSent": time_sent, 
        "TimeRecvd": time_rcvd, 
        "Source": "llama3-70b-8192"
    }
    return obj
#--------------------------------


my_file = open('input.txt', 'r')
line = my_file.readline()

reqd_output = []

while line:

    client = Groq()

    time_sent = time.time()
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": line
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop='.',
    )

    time_rcvd = time.time()

    str = ""
    str += (completion.choices[0].message.content or "")

    reqd_output.append(make_object(str,line,time_sent, time_rcvd))

    line = my_file.readline()


output_file = open('output.json', 'w')
json.dump(reqd_output, output_file)