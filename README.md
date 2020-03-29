# Shamir

## Share a secret.

This program implements a basic version of [Adi Shamir's secret-sharing algorithm](http://users.cms.caltech.edu/~vidick/teaching/101_crypto/Shamir1979.pdf).
You tell the encryption program what your secret message is and how many keys to generate.
The program will then generate those keys, which can be handed out to multiple people.
These keys can be used to decrypt your secret message; however, the decryption algorithm requires **2 keys** to work,
so that no single person can get the secret on their own.
[There must be two people willing to enter their keys](https://www.youtube.com/watch?v=qXkHH6iWKO0).

## Disclaimer
Obviously, if you have a really REALLY important secret then you should NOT use this dinky little program to store it.

## Usage
This program requires Python 3.

To encrypt a message, run `python encrypt.py` from the command line and follow the prompts.

To decrypt a message, run `python decrypt.py` from the command line and follow the prompts.
