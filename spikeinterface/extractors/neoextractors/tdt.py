from .neobaseextractor import NeoBaseRecordingExtractor, NeoBaseSortingExtractor


class TdtRecordingExtractor(NeoBaseRecordingExtractor):
    """
    Class for reading TDT folder

    Based on :py:class:`neo.rawio.TdTRawIO`

    Parameters
    ----------
    folder_path: str
        The tdt folder.
    stream_id: str or None
    """
    mode = 'folder'
    NeoRawIOClass = 'TdtRawIO'

    def __init__(self, folder_path, stream_id=None):
        neo_kwargs = {'dirname': folder_path}
        NeoBaseRecordingExtractor.__init__(self, stream_id=stream_id, **neo_kwargs)

        self._kwargs = dict(folder_path=str(folder_path), stream_id=stream_id)


read_tdt = TdtRecordingExtractor.define_reader_function(name="read_tdt")
