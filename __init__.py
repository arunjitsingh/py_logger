# Copyright 2012 Arunjit Singh. All Rights Reserved.
"""File overview."""

__author__ = 'Arunjit Singh <arunjit@me.com>'

import logging


_BLACK, _RED, _GREEN, _YELLOW, _BLUE, _MAGENTA, _CYAN, _WHITE = range(8)

_RESET_SEQ = "\033[0m"
_COLOR_SEQ = "\033[1;%dm"

_COLORS = {
  'WARNING': _YELLOW,
  'INFO': _GREEN,
  'DEBUG': _BLUE,
  'CRITICAL': _RED,
  'ERROR': _RED
  }


class ColoredFormatter(logging.Formatter):

  def __init__(self, msg):
    super(ColoredFormatter, self).__init__(msg)
    self.use_color = True

  def UseColor(self, use_color):
    self.use_color = use_color

  def format(self, record):
    levelname = record.levelname
    if self.use_color and levelname in _COLORS:
      levelname_color = (_COLOR_SEQ % (30 + _COLORS[levelname]) +
                         levelname + ':' + _RESET_SEQ)
      record.levelname = levelname_color
    return super(ColoredFormatter, self).format(record)


class ColoredLogger(logging.Logger):
  """A log with some color."""

  DEFAULT_FORMAT = '%(levelname)8s <%(filename)s:%(lineno)d> %(message)s'
  LEVEL_ONLY_FORMAT = '%(levelname)8s %(message)s'

  # keep a copy of the levels here
  CRITICAL = logging.CRITICAL
  DEBUG = logging.DEBUG
  ERROR = logging.ERROR
  INFO = logging.INFO
  WARNING = logging.WARNING

  def __init__(self, name=None, level=logging.INFO, fmt=None):
    super(ColoredLogger, self).__init__(name, level)
    self.format = fmt or ColoredLogger.DEFAULT_FORMAT
    self.ResetLogger()

  def SetFormat(self, fmt):
    self.format = fmt
    self.ResetLogger()

  def ResetLogger(self):
    self._formatter = ColoredFormatter(self.format)
    self._console_handler = logging.StreamHandler()
    self._console_handler.setFormatter(self._formatter)
    self.addHandler(self._console_handler)

  def UseColor(self, use_color):
    self._formatter.UseColor(use_color)


logger = ColoredLogger(fmt=ColoredLogger.LEVEL_ONLY_FORMAT)
