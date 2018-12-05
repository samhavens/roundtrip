## roundtrip

Round-trip translation, aka back-translation, using Google's Translate API.

### Why

Translating a phrase to another language and back, called back-translation, is a good way to generate more training data for NLP models.

### Notice

This is just a hack for one-off examples. It uses the API in a way that may not have been intended. For any large-scale translation, you should use the [Cloud Translation API](https://cloud.google.com/translate/docs/) which is fast and reasonably priced.

The plan is to replace the implementation under the hood to use the official API, but this is the POC.

