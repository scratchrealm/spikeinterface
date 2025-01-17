from .neobaseextractor import NeoBaseRecordingExtractor, NeoBaseSortingExtractor


class SpikeGadgetsRecordingExtractor(NeoBaseRecordingExtractor):
    """
    Class for reading *rec files from spikegadgets.

    
    Parameters
    ----------
    file_path: str
        The smr or smrx  file.
    stream_id: str or None
    """
    mode = 'file'
    NeoRawIOClass = 'SpikeGadgetsRawIO'

    def __init__(self, file_path, stream_id=None):
        neo_kwargs = {'filename': str(file_path)}
        NeoBaseRecordingExtractor.__init__(self, stream_id=stream_id, **neo_kwargs)

        self._kwargs = dict(file_path=str(file_path), stream_id=stream_id)


read_spikegadgets = SpikeGadgetsRecordingExtractor.define_reader_function(name="read_spikegadgets")
