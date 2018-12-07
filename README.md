## roundtrip

Round-trip translation, aka back-translation, using Google's Translate API.

### Why

Data Augmentation - translating a phrase to another language and back, called back-translation, is a good way to generate more training data for NLP models.

### Notice

The CLI is just a hack for one-off examples. It uses the API in a way that may not have been intended. For any large-scale translation, you should use the [Cloud Translation API](https://cloud.google.com/translate/docs/) which is fast and reasonably priced.

If the ENV variable `GOOGLE_APPLICATION_CREDENTIALS` is set, it will use the official Google Translate API with the credentials it finds in `GOOGLE_APPLICATION_CREDENTIALS`.

### Usage

Install

```sh
pip install roundtrip
```

To play around on the CLI, use like this:

```sh
Usage:
$ roundtrip text_to_translate to_lang from_lang
from_lang is optional
to_lang is required
Example:
$ roundtrip "Returns the translation using google translate you must shortcut the language you define" fr
Returns the translation using Google Translate, you must shorten the language you set
```

However, if you want to call from `myscript.py`:

```py
from roundtrip import backtranslate

back = backtranslate("this is a phrase in my NLP training data", "de")
print(back)
>>> "This is a sentence in my NLP training data"

# now go augment your training data
```

If the env var `GOOGLE_APPLICATION_CREDENTIALS` is set, the python snippet above will use the official translate API and you will be charged. So call it like this:

```sh
$ GOOGLE_APPLICATION_CREDENTIALS='/home/users/example.json' myscript.py
```

You get the credential file from [The Google Cloud Console](https://console.developers.google.com/apis/api/translate.googleapis.com/overview).

### Developing

If you want to add to this package, be aware that the `package_and_release.sh` script is pretty janky. Currently you need to bump the version and git commit by hand.
