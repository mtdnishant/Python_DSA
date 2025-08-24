# Circular Linked List in Python

## 📘 Circular Linked List क्या है?

Circular Linked List एक प्रकार की लिंक्ड लिस्ट है जिसमें आखिरी नोड का `next` पॉइंटर पहले नोड की ओर इशारा करता है, जिससे यह एक वृत्त (circle) बनाता है। यह संरचना विशेष रूप से तब उपयोगी होती है जब हमें लिस्ट को बार-बार दोहराना हो, जैसे Round-Robin शेड्यूलिंग में।

## 🧱 संरचना

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
