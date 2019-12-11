from google.cloud import speech_v1

storage_uri = 'gs://cloud-samples-data/speech/brooklyn_bridge.flac'

def sample_long_running_recognize(storage_uri):
    """
    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
    """

    client = speech_v1.SpeechClient()



    # When enabled, the first result returned by the API will include a list
    # of words and the start and end time offsets (timestamps) for those words.
    enable_word_time_offsets = True

    # The language of the supplied audio
    language_code = "en-US"
    config = {
        "enable_word_time_offsets": enable_word_time_offsets,
        "language_code": language_code,
    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    print(u"Waiting for operation to complete...")
    response = operation.result()

    # The first result includes start and end time word offsets
    result = response.results[0]
    # First alternative is the most probable result
    alternative = result.alternatives[0]
    print(u"Transcript: {}".format(alternative.transcript))
    # Print the start and end time of each word
    for word in alternative.words:
        print(u"Word: {}".format(word.word))
        print(
            u"Start time: {} seconds {} nanos".format(
                word.start_time.seconds, word.start_time.nanos
            )
        )
        print(
            "End time: {} seconds {} nanos".format(
                word.end_time.seconds, word.end_time.nanos
            )
        )
sample_long_running_recognize(storage_uri)
