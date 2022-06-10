from typing import Union


def _get_plot_mode(plot_mode: Union[str, None]):
    if plot_mode is None:
        return 'matplotlib'
    else:
        return plot_mode