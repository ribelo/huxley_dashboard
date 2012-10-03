#-*- coding: utf-8-*-

import math
import csv
import datetime

class CandleException(Exception):
    """docstring for CandleException"""
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return repr(self.text)


class Candle(object):
    """docstring for Candle"""

    db = {}

    @classmethod
    def open(cls, broker, symbol, timeframe, no):
        return cls.reframe(broker, symbol, timeframe, 'open', no)

    @classmethod
    def high(cls, broker, symbol, timeframe, no):
        return cls.reframe(broker, symbol, timeframe, 'high', no)

    @classmethod
    def low(cls, broker, symbol, timeframe, no):
        return cls.reframe(broker, symbol, timeframe, 'low', no)

    @classmethod
    def close(cls, broker, symbol, timeframe, no):
        return cls.reframe(broker, symbol, timeframe, 'close', no)

    @classmethod
    def vol(cls, broker, symbol, timeframe, no):
        return cls.reframe(broker, symbol, timeframe, 'vol', no)

    @classmethod
    def bodySize(cls, broker, symbol, timeframe, no):
        return math.fabs(cls.close(broker, symbol, timeframe, no) - cls.open(broker, symbol, timeframe, no))

    @classmethod
    def upShadowSize(cls, broker, symbol, timeframe, no):
        return cls.high(broker, symbol, timeframe, no) - max([cls.close(broker, symbol, timeframe, no), cls.open(broker, symbol, timeframe, no)])

    @classmethod
    def dnShadowSize(cls, broker, symbol, timeframe, no):
        return min([cls.close(broker, symbol, timeframe, no), cls.open(broker, symbol, timeframe, no)]) - cls.low(broker, symbol, timeframe, no)

    @classmethod
    def barSize(cls, broker, symbol, timeframe, no):
        return cls.high(broker, symbol, timeframe, no) - cls.low(broker, symbol, timeframe, no)

    @classmethod
    def point(cls, broker, symbol, timeframe, no, mode='body', point=0.5):
        if mode == 'body':
            return point * (cls.close(broker, symbol, timeframe, no) + cls.open(broker, symbol, timeframe, no))
        elif mode == 'bar':
            return point * (cls.high(broker, symbol, timeframe, no) + cls.low(broker, symbol, timeframe, no))

    @classmethod
    def highest(cls, broker, symbol, timeframe, mode, count, start):
        cls.validateIndex(broker, symbol, start)
        stop = min([start + count, cls.maxIndex(broker, symbol)])
        col = cls.getColumn(mode)
        arr = [val[col] for val in cls.db[broker][symbol]['quote'][start:stop]]
        return arr.index(max(arr))

    @classmethod
    def lowest(cls, broker, symbol, timeframe, mode, count, start):
        cls.validateIndex(broker, symbol, start)
        stop = min([start + count, cls.maxIndex(broker, symbol)])
        col = cls.getColumn(mode)
        arr = [val[col] for val in cls.db[broker][symbol]['quote'][start:stop]]
        return arr.index(min(arr))

    @classmethod
    def biggest(cls, broker, symbol, timeframe, mode, count, start):
        cls.validateIndex(broker, symbol, start)
        stop = min([start + count, cls.maxIndex(broker, symbol)])
        if mode == 'body':
            hh = cls.getColumn('close')
            ll = cls.getColumn('open')
        elif mode == 'bar':
            hh = cls.getColumn('high')
            ll = cls.getColumn('low')
        elif mode == 'upShadow':
            hh = cls.getColumn('high')
        elif mode == 'dnShadow':
            ll = cls.getColumn('low')

        val = 0
        val_no = 0
        if mode == 'body' or mode == 'bar':
            h_arr = [val[hh] for val in cls.db[broker][symbol]['quote'][start:stop]]
            l_arr = [val[ll] for val in cls.db[broker][symbol]['quote'][start:stop]]
            for x in range(count):
                if math.fabs(h_arr[x] - l_arr[x]) > val:
                    val = math.fabs(h_arr[x] - l_arr[x])
                    val_no = x
            return val_no + start
        elif mode == 'upshadow':
            h_arr = [val[hh] for val in cls.db[broker][symbol]['quote'][start:stop]]
            l_arr = [val[max([cls.getColumn('close'), cls.getColumn('open')])] for val in cls.db[broker][symbol]['quote'][start:stop]]
            for x in range(count):
                if h_arr[x] - l_arr[x] > val:
                    val = math.fabs(h_arr[x] - l_arr[x])
                    val_no = x
            return val_no + start
        elif mode == 'dnShadow':
            h_arr = [val[min([cls.getColumn('close'), cls.getColumn('open')])] for val in cls.db[broker][symbol]['quote'][start:stop]]
            l_arr = [val[ll] for val in cls.db[broker][symbol]['quote'][start:stop]]
            for x in range(count):
                if math.fabs(h_arr[x] - l_arr[x]) > val:
                    val = math.fabs(h_arr[x] - l_arr[x])
                    val_no = x
            return val_no + start

    @classmethod
    def bigBody(cls, broker, symbol, timeframe, count, start):
        return cls.bodySize(broker, symbol, timeframe, cls.biggest(broker, symbol, timeframe, 'body', count, start))

    @classmethod
    def bigBar(cls, broker, symbol, timeframe, count, start):
        return cls.barSize(broker, symbol, timeframe, cls.biggest(broker, symbol, timeframe, 'bar', count, start))

    @classmethod
    def smallBody(cls, broker, symbol, timeframe, count, start):
        return cls.bodySize(broker, symbol, timeframe, cls.smallest(broker, symbol, timeframe, 'body', count, start))

    @classmethod
    def smallBar(cls, broker, symbol, timeframe, count, start):
        return cls.barSize(broker, symbol, timeframe, cls.smallest(broker, symbol, timeframe, 'bar', count, start))

    @classmethod
    def smallest(cls, broker, symbol, timeframe, mode, count, start):
        cls.validateIndex(broker, symbol, start)
        stop = min([start + count, cls.maxIndex(broker, symbol)])
        if mode == 'body':
            hh = cls.getColumn('close')
            ll = cls.getColumn('open')
        elif mode == 'bar':
            hh = cls.getColumn('high')
            ll = cls.getColumn('low')

        val = 0
        val_no = 0
        h_arr = [val[hh] for val in cls.db[broker][symbol]['quote'][start:stop]]
        l_arr = [val[ll] for val in cls.db[broker][symbol]['quote'][start:stop]]
        for x in range(count):
            if math.fabs(h_arr[x] - l_arr[x]) < val:
                val = math.fabs(h_arr[x] - l_arr[x])
                val_no = x

        return val_no + start

    @classmethod
    def rising(cls, broker, symbol, timeframe, no):
        if cls.close(broker, symbol, timeframe, no) > cls.open(broker, symbol, timeframe, no):
            return True
        return False

    @classmethod
    def falling(cls, broker, symbol, timeframe, no):
        if cls.close(broker, symbol, timeframe, no) < cls.open(broker, symbol, timeframe, no):
            return True
        return False

    @classmethod
    def equal(clse, broker, symbol, timeframe, no):
        if cls.close(broker, symbol, timeframe, no) == cls.open(broker, symbol, timeframe, no):
            return True
        return False

    @classmethod
    def filled(cls, broker, symbol, timeframe, v1, v2):
        if cls.rising(broker, symbol, timeframe, v2):
            if cls.open(broker, symbol, timeframe, v2) >= cls.low(broker, symbol, timeframe, cls.lowest(broker, symbol, timeframe, 'low', v2 - v1 - 1, v1 + 1)):
                return True
        if cls.falling(broker, symbol, timeframe, v2):
            if cls.open(broker, symbol, timeframe, v2) <= cls.high(broker, symbol, timeframe, cls.highest(broker, symbol, timeframe, 'high', v2 - v1 - 1, v1 + 1)):
                return True
        return False

    @classmethod
    def share(cls, broker, symbol, timeframe, v1, v2):
        if cls.rising(broker, symbol, timeframe, v2):
            if cls.high(broker, symbol, timeframe, v2) >= cls.low(broker, symbol, timeframe, cls.lowest(broker, symbol, timeframe, 'low', v2 - v1 - 1, v1 + 1)) and cls.low(broker, symbol, timeframe, v1) <= cls.high(broker, symbol, timeframe, cls.highest(broker, symbol, timeframe, 'high', v2 - v1 - 1, v1 + 1)):
                return True
        if cls.falling(broker, symbol, timeframe, v2):
            if cls.low(broker, symbol, timeframe, v2) <= cls.high(broker, symbol, timeframe, cls.highest(broker, symbol, timeframe, 'high', v2 - v1 - 1, v1 + 1)) and cls.high(broker, symbol, timeframe, v1) >= cls.low(broker, symbol, timeframe, cls.lowest(broker, symbol, timeframe, 'low', v2 - v1 - 1, v1 + 1)):
                return True
        return False

    @classmethod
    def breakOut(cls, broker, symbol, timeframe, count, no):
        if cls.rising(broker, symbol, timeframe, no):
            if cls.close(broker, symbol, timeframe, no) > cls.high(broker, symbol, timeframe, cls.highest(broker, symbol, timeframe, 'high', count, no + 1)):
                return True
        if cls.falling(broker, symbol, timeframe, no):
            if cls.close(broker, symbol, timeframe, no) < cls.low(broker, symbol, timeframe, cls.lowest(broker, symbol, timeframe, 'low', count, no + 1)):
                return True
        return False

    @classmethod
    def overlap(cls, broker, symbol, timeframe, no):
        if cls.rising(broker, symbol, timeframe, no):
            if max(cls.high(broker, symbol, timeframe, no + 1), cls.open(broker, symbol, timeframe, no)) >= min(cls.low(broker, symbol, timeframe, no - 1), cls.close(broker, symbol, timeframe, no)):
                return True
        if cls.falling(broker, symbol, timeframe, no):
            if min(cls.low(broker, symbol, timeframe, no + 1), cls.open(broker, symbol, timeframe, no)) <= max(cls.high(broker, symbol, timeframe, no - 1), cls.close(broker, symbol, timeframe, no)):
                return True
        return False

    @classmethod
    def breakReaction(cls, broker, symbol, timeframe, no):
        if cls.rising(broker, symbol, timeframe, no):
            reaction_high = 0
            rising = 0
            falling = 0
            for x in range(no + 1, cls.maxIndex(broker, symbol)):
                reaction_high = max(reaction_high, cls.high(broker, symbol, timeframe, x))
                if cls.falling(broker, symbol, timeframe, x):
                    falling = falling + 1
                elif falling < 2:
                    falling = 0
                if falling >= 2:
                    if reaction_high >= cls.close(broker, symbol, timeframe, no):
                        return False
                    if cls.high(broker, symbol, timeframe, x) <= cls.open(broker, symbol, timeframe, no):
                        continue
                    for y in range(x + 1, cls.maxIndex(broker, symbol)):
                        if cls.close(broker, symbol, timeframe, y) > cls.close(broker, symbol, timeframe, x):
                            break
                        if cls.rising(broker, symbol, timeframe, y):
                            rising = rising + 1
                        elif rising < 2:
                            rising = 0
                        if rising >= 2:
                            return True
            return False

        elif cls.falling(broker, symbol, timeframe, no):
            reaction_low = 9999
            rising = 0
            falling = 0
            for x in range(no + 1, cls.maxIndex(broker, symbol)):
                reaction_low = min(reaction_low, cls.low(broker, symbol, timeframe, x))
                if cls.rising(broker, symbol, timeframe, x):
                    rising = rising + 1
                elif rising < 2:
                    rising = 0
                if rising >= 2:
                    if reaction_low <= cls.close(broker, symbol, timeframe, no):
                        return False
                    if cls.low(broker, symbol, timeframe, x) >= cls.open(broker, symbol, timeframe, no):
                        continue
                    for y in range(x + 1, cls.maxIndex(broker, symbol)):
                        if cls.close(broker, symbol, timeframe, y) < cls.close(broker, symbol, timeframe, x):
                            break
                        if cls.falling(broker, symbol, timeframe, y):
                            falling = falling + 1
                        elif falling < 2:
                            falling = 0
                        if falling >= 2:
                            return True
            return False

    @classmethod
    def withinRange(cls, broker, symbol, timeframe, mode, v1, *args):
        if mode == 'body':
            high = max([cls.open(broker, symbol, timeframe, x) for x in args] + [cls.close(broker, symbol, timeframe, x) for x in args])
            low = min([cls.open(broker, symbol, timeframe, x) for x in args] + [cls.close(broker, symbol, timeframe, x) for x in args])
        elif mode == 'bar':
            high = max([cls.high(broker, symbol, timeframe, x) for x in args])
            low = min([cls.low(broker, symbol, timeframe, x) for x in args])

        if cls.rising(broker, symbol, timeframe, v1):
            if cls.open(broker, symbol, timeframe, no) > low and cls.close(broker, symbol, timeframe, v1) < high:
                return True
        elif cls.falling(broker, symbol, timeframe, v1):
            if cls.open(broker, symbol, timeframe, no) < high and cls.close(broker, symbol, timeframe, v1) > low:
                return True
        return False

    @classmethod
    def doji(cls, broker, symbol, timeframe, no):
        if cls.open(broker, symbol, timeframe, no) == cls.close(broker, symbol, timeframe, no):
            return True
        return False

    @classmethod
    def longShadow(cls, broker, symbol, timeframe, mode, no):
        if mode == 'dn':
            shadow = min([cls.close(broker, symbol, timeframe, no), cls.open(broker, symbol, timeframe, no)]) - cls.low(broker, symbol, timeframe, no)
        elif mode == 'up':
            shadow = cls.high(broker, symbol, timeframe, no) - max([cls.close(broker, symbol, timeframe, no), cls.open(broker, symbol, timeframe, no)])
        body = abs(cls.close(broker, symbol, timeframe, no) - cls.open(broker, symbol, timeframe, no))
        if shadow > body:
            return True
        return False

    @classmethod
    def reframe(cls, broker, symbol, timeframe, mode, no):
        cls.validateIndex(broker, symbol, no)
        col = cls.getColumn(mode)
        if timeframe > 1:
            return cls.retimeframe(broker, symbol, timeframe, mode, no)
        else:
            return cls.db[broker][symbol]['quote'][no][col]

    @classmethod
    def retimeframe(cls, broker, symbol, timeframe, mode, no):
        cls.validateIndex(broker, symbol, no)
        col = cls.getColumn(mode)
        row = 0
        old_minutes = cls.db[broker][symbol]['quote'][no][0]
        for val in cls.db[broker][symbol]['quote']:
            time_tuple = val[0].timetuple()
            if time_tuple[4] % timeframe == 0 or time_tuple[4] == 0:
                if no == 0:
                    return val[col]
                else:
                    print(time_tuple[4], row, no)
                    Candle.validateIndex(broker, symbol, row + timeframe * no)
                    return cls.db[broker][symbol]['quote'][row + timeframe * no][col]
            else:
                row = row + 1

    @classmethod
    def getColumn(cls, mode):
        if mode == 'vol':
            return 1
        elif mode == 'open':
            return 2
        elif mode == 'high':
            return 3
        elif mode == 'low':
            return 4
        elif mode == 'close':
            return 5

    @classmethod
    def validateIndex(cls, broker, symbol, *args):
        for x in args:
            if x < 0 or x >= cls.maxIndex(broker, symbol):
                raise IndexError('Candle {0} does not exist'.format(x))

    @classmethod
    def maxIndex(cls, broker, symbol):
        return len(cls.db[broker][symbol]['quote']) - 1

    @classmethod
    def timeToIndex(cls, broker, symbol, time):
        for row in cls.db[broker][symbol]['quote']:
            if row[0] == time:
                return cls.db[broker][symbol]['quote'].index(row)

    @classmethod
    def indexToTime(cls, broker, symbol, no):
        return cls.db[broker][symbol]['quote'][no][0]


class WRB(object):
    """docstring for WRB"""

    db = {'WRB': {}, 'ZONE': {}, 'AJCTR': {}, 'APAOR': {}, 'STR': {}, 'FVB': {}}

    @classmethod
    def bullWRB(cls, broker, symbol, timeframe, no):
        try:
            if Candle.bodySize(broker, symbol, timeframe, no) > max([Candle.bodySize(broker, symbol, timeframe, x) for x in range(no + 1, no + 1 + Settings.options['wrb_size'])]):
                if Candle.rising(broker, symbol, timeframe, no):
                    if Candle.breakOut(broker, symbol, timeframe, Settings.options['wrb_size'], no):
                        return True
            return False
        except IndexError:
            return False

    @classmethod
    def bullHG(cls, broker, symbol, timeframe, no):
        if no == 1:
            return False
        try:
            if cls.bullWRB(broker, symbol, timeframe, no):
                if not Candle.overlap(broker, symbol, timeframe, no):
                    return True
            return False
        except IndexError:
            return False

    @classmethod
    def bearWRB(cls, broker, symbol, timeframe, no):
        try:
            if Candle.bodySize(broker, symbol, timeframe, no) > max([Candle.bodySize(broker, symbol, timeframe, x) for x in range(no + 1, no + 1 + Settings.options['wrb_size'])]):
                if Candle.falling(broker, symbol, timeframe, no):
                    if Candle.breakOut(broker, symbol, timeframe, Settings.options['wrb_size'], no):
                        return True
            return False
        except IndexError:
            return False

    @classmethod
    def bearHG(cls, broker, symbol, timeframe, no):
        if no == 1:
            return False
        try:
            if cls.bearWRB(broker, symbol, timeframe, no):
                if not Candle.overlap(broker, symbol, timeframe, no):
                    return True
            return False
        except IndexError:
            return False

    @classmethod
    def bullSwingPoint1(cls, broker, symbol, timeframe, v1):
        if v1 < 2:
            return False
        try:
            # Bearish Swing Point
            if cls.bullHG(broker, symbol, timeframe, v1):
                bull_count = 0
                # Must be two consecutive white canldes after and belove V1
                for x in range(v1 - 1, v1 - 1 - Settings.options['candle_lookback'], -1):
                    if Candle.low(broker, symbol, timeframe, x) <= Candle.open(broker, symbol, timeframe, v1):
                        return False
                    if Candle.rising(broker, symbol, timeframe, x) and Candle.close(broker, symbol, timeframe, x) > Candle.close(broker, symbol, timeframe, v1):

                        bull_count = bull_count + 1
                    else:
                        bull_count = 0
                    if bull_count >= 2:
                        break
                if bull_count < 2:
                    return False
                # Look for V2
                for v2 in range(v1 + 4, v1 + 4 + Settings.options['candle_lookback']):
                    if cls.bearWRB(broker, symbol, timeframe, v2):
                        # V1 must be breakout volatility contraction
                        if not Candle.breakOut(broker, symbol, timeframe, v2 - v1, v1):
                            # return False
                            continue
                        #  Contraction volatiliti must share min 1 pip with V2
                        if not Candle.share(broker, symbol, timeframe, v1, v2):
                            # return False
                            continue
                        # V2 must be unfilled
                        if Candle.filled(broker, symbol, timeframe, v1, v2):
                            # return False
                            continue
                        if min([Candle.bodySize(broker, symbol, timeframe, v1), Candle.bodySize(broker, symbol, timeframe, v2)]) < Candle.bigBody(broker, symbol, timeframe, v2 - v1 - 1, v1 + 1):
                            # return False
                            continue
                        # Price action must fill prior Bear WRB HG. Thus, the prior WRB HG must occur before the v2 WRB
                        for x in range(v2 + 2, v2 + 2 + Settings.options['candle_lookback']):
                            if cls.bearHG(broker, symbol, timeframe, x):
                                for y in range(v1 - 1, v1 - 1 - Settings.options['candle_lookback'], -1):
                                    if Candle.low(broker, symbol, timeframe, y) <= Candle.open(broker, symbol, timeframe, v1):
                                        return False
                                    if Candle.filled(broker, symbol, timeframe, y, x):
                                        return True
                    elif cls.bullHG(broker, symbol, timeframe, v2):
                        swing_point_low = Candle.low(broker, symbol, timeframe, Candle.lowest(broker, symbol, timeframe, 'low', 2, v1))
                        for x in range(v2 + 2, v2 + 2 + Settings.options['candle_lookback']):
                            if Candle.low(broker, symbol, timeframe, x) > swing_point_low:
                                return False
                            if Candle.high(broker, symbol, timeframe, x) > Candle.close(broker, symbol, timeframe, v1):
                                return True
                            if cls.bearHG(broker, symbol, timeframe, x):
                                return True
            return False
        except IndexError:
            return False

    @classmethod
    def bearSwingPoint1(cls, broker, symbol, timeframe, v1):
        if v1 < 2:
            return False
        try:
            # Bearish Swing Point
            if cls.bearHG(broker, symbol, timeframe, v1):
                bear_count = 0
                # Must be two consecutive dak canldes after and belove V1
                for x in range(v1 - 1, v1 - 1 - Settings.options['candle_lookback'], -1):
                    if Candle.high(broker, symbol, timeframe, x) >= Candle.open(broker, symbol, timeframe, v1):
                        return False
                    if Candle.falling(broker, symbol, timeframe, x) and Candle.close(broker, symbol, timeframe, x) < Candle.close(broker, symbol, timeframe, v1):
                        bear_count = bear_count + 1
                    else:
                        bear_count = 0
                    if bear_count >= 2:
                        break
                if bear_count < 2:
                    return False
                # Look for V2
                for v2 in range(v1 + 4, v1 + 4 + Settings.options['candle_lookback']):
                    if cls.bullWRB(broker, symbol, timeframe, v2):
                        # V1 must be breakout volatility contraction
                        if not Candle.breakOut(broker, symbol, timeframe, v2 - v1, v1):
                            return False
                        #  Contraction volatiliti must share min 1 pip with V2
                        if not Candle.share(broker, symbol, timeframe, v1, v2):
                            return False
                        # V2 must be unfilled
                        if Candle.filled(broker, symbol, timeframe, v1, v2):
                            return False
                        if min([Candle.bodySize(broker, symbol, timeframe, v1), Candle.bodySize(broker, symbol, timeframe, v2)]) < Candle.bigBody(broker, symbol, timeframe, v2 - v1 - 1, v1 + 1):
                            return False
                        # Price action must fill prior Bull WRB HG. Thus, the prior WRB HG must occur before the v2 WRB
                        for x in range(v2 + 2, v2 + 2 + Settings.options['candle_lookback']):
                            if cls.bullHG(broker, symbol, timeframe, x):
                                for y in range(v1 - 1, v1 - 1 - Settings.options['candle_lookback'], -1):
                                    if Candle.high(broker, symbol, timeframe, y) >= Candle.open(broker, symbol, timeframe, v1):
                                        return False
                                    if Candle.filled(broker, symbol, timeframe, y, x):
                                        return True
                    elif cls.bearHG(broker, symbol, timeframe, v2):
                        swing_point_high = Candle.high(broker, symbol, timeframe, Candle.highest(broker, symbol, timeframe, 'high', 2, v1))
                        for x in range(v2 + 2, v2 + 2 + Settings.options['candle_lookback']):
                            if Candle.high(broker, symbol, timeframe, x) > swing_point_high:
                                return False
                            if Candle.low(broker, symbol, timeframe, x) < Candle.close(broker, symbol, timeframe, v1):
                                return True
                            if cls.bullHG(broker, symbol, timeframe, x):
                                return True
            return False
        except IndexError:
            return False

    @classmethod
    def bullSwingPoint2(cls, broker, symbol, timeframe, v1):
        try:
            if cls.bullHG(broker, symbol, timeframe, v1):
                # Must produce two consecutive white canldes after and above V1
                if any([Candle.rising(broker, symbol, timeframe, x) for x in range(v1 - 1, v1 - 3, -1)]) or min([Candle.low(broker, symbol, timeframe, x) for x in range(v1 - 1, v1 - 3, -1)]) <= Candle.open(broker, symbol, timeframe, v1):
                    return False
                for v2 in range(v1 + 4, Candle.maxIndex(broker, symbol)):
                    if cls.bearWRB(broker, symbol, timeframe, v2):
                        # V1 must be breakout volatility contraction
                        if not Candle.breakOut(broker, symbol, timeframe, v2 - v1 - 1, v1):
                            return False
                        # Contraction volatiliti must share min 1 pip with V2.
                        if not Candle.share(broker, symbol, timeframe, v1, v2):
                            return False
                        if min(Candle.bodySize(broker, symbol, timeframe, v1), Candle.bodySize(broker, symbol, timeframe, v2)) <= Candle.bigBody(broker, symbol, timeframe, v2 - v1 - 1, v1 + 1):
                            return False
                        return True
            return False
        except IndexError:
            return False

    @classmethod
    def bearSwingPoint2(cls, broker, symbol, timeframe, v1):
        try:
            if cls.bearHG(broker, symbol, timeframe, v1):
                # Must produce two consecutive white canldes after and above V1
                if any([Candle.falling(broker, symbol, timeframe, x) for x in range(v1 - 1, v1 - 3, -1)]) or max([Candle.high(broker, symbol, timeframe, x) for x in range(v1 - 1, v1 - 3, -1)]) >= Candle.open(broker, symbol, timeframe, v1):
                    return False
                for v2 in range(v1 + 4, Candle.maxIndex(broker, symbol)):
                    if cls.bullWRB(broker, symbol, timeframe, v2):
                        # V1 must be breakout volatility contraction
                        if not Candle.breakOut(broker, symbol, timeframe, v2 - v1 - 1, v1):
                            return False
                        # Contraction volatiliti must share min 1 pip with V2.
                        if not Candle.share(broker, symbol, timeframe, v1, v2):
                            return False
                        if min(Candle.bodySize(broker, symbol, timeframe, v1), Candle.bodySize(broker, symbol, timeframe, v2)) <= Candle.bigBody(broker, symbol, timeframe, v2 - v1 - 1, v1 + 1):
                            return False
                        return True
            return False
        except IndexError:
            return False

    @classmethod
    def bullStrongContinuation1(cls, broker, symbol, timeframe, v1):
        if cls.bullHG(broker, symbol, timeframe, v1):
            for v2 in range(v1 + 4, Candle.maxIndex(broker, symbol)):
                if cls.bullHG(broker, symbol, timeframe, v2):
                    # V1 must be breakout volatility contraction
                    if not Candle.breakOut(broker, symbol, timeframe, v2 - v1 - 1, v1):
                        return False
                    # Contraction volatiliti must share min 1 pip with V2.
                    if not Candle.share(broker, symbol, timeframe, v1, v2):
                        return False
                    # Body of V1 and V2 must be bigger than bigest body in volatility contraction
                    if min(Candle.bodySize(broker, symbol, timeframe, v1), Candle.bodySize(broker, symbol, timeframe, v2)) <= Candle.bigBody(broker, symbol, timeframe, v2 - v1 - 1, v1 + 1):
                        return False
                    # V1 or V2 must break reaction high
                    if Candle.breakReaction(broker, symbol, timeframe, v2) or Candle.breakReaction(broker, symbol, timeframe, v1):
                        return True
        return False

    @classmethod
    def bearStrongContinuation1(cls, broker, symbol, timeframe, v1):
        if cls.bearHG(broker, symbol, timeframe, v1):
            for v2 in range(v1 + 4, Candle.maxIndex(broker, symbol)):
                if cls.bearHG(broker, symbol, timeframe, v2):
                    # V1 must be breakout volatility contraction
                    if not Candle.breakOut(broker, symbol, timeframe, v2 - v1 - 1, v1):
                        return False
                    # Contraction volatiliti must share min 1 pip with V2.
                    if not Candle.share(broker, symbol, timeframe, v1, v2):
                        return False
                    if min(Candle.bodySize(broker, symbol, timeframe, v1), Candle.bodySize(broker, symbol, timeframe, v2)) <= Candle.bigBody(broker, symbol, timeframe, v2 - v1 - 1, v1 + 1):
                        return False
                    # V1 or V2 must break reaction low
                    if Candle.breakReaction(broker, symbol, timeframe, v2) or Candle.breakReaction(broker, symbol, timeframe, v1):
                        return True
        return False

    @classmethod
    def bullStrongContinuation2(cls, broker, symbol, timeframe, v1):
        if cls.bullHG(broker, symbol, timeframe, v1):
            # Must be minimum two white lines with higher closes after and above the close of the v1 White WRB prior to the next swing point.
            rising_count = 0
            for x in range(v1 - 1, 0, - 1):
                if Candle.rising(broker, symbol, timeframe, x):
                    rising_count = rising_count + 1
                if rising_count < 2:
                    if any([cls.bearSwingPoint1(broker, symbol, timeframe, x), cls.bearSwingPoint2(broker, symbol, timeframe, x)]):
                        return False
                else:
                    break
            # Look for v2
            for v2 in range(v1 + 4, Candle.maxIndex(broker, symbol)):

                if cls.bullWRB(broker, symbol, timeframe, v2):
                    if not Candle.breakOut(broker, symbol, timeframe, v2 - v1 - 1, v1):
                        return False
                    if Candle.filled(broker, symbol, timeframe, v1, v2):
                        return False
                    if not Candle.share(broker, symbol, timeframe, v1, v2):
                        return False
                    if min(Candle.bodySize(broker, symbol, timeframe, v1), Candle.bodySize(broker, symbol, timeframe, v2)) <= Candle.bigBody(broker, symbol, timeframe, v2 - v1 - 1, v1 + 1):
                        return False
                    # Must be minimum two white lines with higher closes before and belove the close of the v2 Dark WRB.
                    if len([val == True for val in [Candle.rising(broker, symbol, timeframe, x) for x in range(v1 + 1, v1 + 13) if Candle.close(broker, symbol, timeframe, x) < Candle.close(broker, symbol, timeframe, v1)]]) < 2:
                        return False
                    # Must be minimum two white lines with higher closes after and above the close of the v2 Dark WRB.
                    if len([val == True for val in [Candle.rising(broker, symbol, timeframe, x) for x in range(v1 - 1, v1 - 13, -1) if Candle.close(broker, symbol, timeframe, x) > Candle.close(broker, symbol, timeframe, v1)]]) < 2:
                        return False
                    return True
        return False

    @classmethod
    def bearStrongContinuation2(cls, broker, symbol, timeframe, v1):
        if cls.bearHG(broker, symbol, timeframe, v1):
            # Must be minimum two white lines with lower closes after and belove the close of the v1 White WRB prior to the next swing point.
            falling_count = 0
            for x in range(v1 - 1, 0, - 1):
                if Candle.falling(broker, symbol, timeframe, x):
                    falling_count = falling_count + 1
                if falling_count < 2:
                    if any([cls.bullSwingPoint1(broker, symbol, timeframe, x), cls.bullSwingPoint2(broker, symbol, timeframe, x)]):
                        return False
                else:
                    break
            # Look for v2
            for v2 in range(v1 + 4, Candle.maxIndex(broker, symbol)):
                if cls.bearWRB(broker, symbol, timeframe, v2):
                    if not Candle.breakOut(broker, symbol, timeframe, v2 - v1 - 1, v1):
                        return False
                    if Candle.filled(broker, symbol, timeframe, v1, v2):
                        return False
                    if not Candle.share(broker, symbol, timeframe, v1, v2):
                        return False
                    if min(Candle.bodySize(broker, symbol, timeframe, v1), Candle.bodySize(broker, symbol, timeframe, v2)) <= Candle.bigBody(broker, symbol, timeframe, v2 - v1 - 1, v1 + 1):
                        return False
                    # Must be minimum two dark lines with lower closes before and above the close of the v2 Dark WRB.
                    if len([val == True for val in [Candle.falling(broker, symbol, timeframe, x) for x in range(v1 + 1, v1 + 13) if Candle.close(broker, symbol, timeframe, x) > Candle.close(broker, symbol, timeframe, v1)]]) < 2:
                        return False
                    # Must be minimum two dark lines with lower closes after and belove the close of the v2 Dark WRB.
                    if len([val == True for val in [Candle.falling(broker, symbol, timeframe, x) for x in range(v1 - 1, v1 - 13, -1) if Candle.close(broker, symbol, timeframe, x) < Candle.close(broker, symbol, timeframe, v1)]]) < 2:
                        return False
                    return True
        return False

    @classmethod
    def bullStrongContinuation3(cls, broker, symbol, timeframe, v1):
        if cls.bullHG(broker, symbol, timeframe, v1):
            # Look for v2
            for v2 in range(v1 + 4, Candle.maxIndex(broker, symbol)):
                if cls.bullHG(broker, symbol, timeframe, v2):
                    if not Candle.breakOut(broker, symbol, timeframe, v2 - v1 - 1, v1):
                        return False
                    if not Candle.share(broker, symbol, timeframe, v1, v2):
                        return False
                    if min(Candle.bodySize(broker, symbol, timeframe, v1), Candle.bodySize(broker, symbol, timeframe, v2)) <= Candle.bigBody(broker, symbol, timeframe, v2 - v1 - 1, v1 + 1):
                        return False
                    if any([Candle.point(broker, symbol, timeframe, v1) > Candle.highest(broker, symbol, timeframe, 'close', v2 - v1 - 1, v1 + 1), Candle.point(broker, symbol, timeframe, v2) < Candle.lowest(broker, symbol, timeframe, 'close', v2 - v1 - 1, v1 + 1)]):
                        return False
                    return True
        return False

    @classmethod
    def bearStrongContinuation3(cls, broker, symbol, timeframe, v1):
        if cls.bearHG(broker, symbol, timeframe, v1):
            # Look for v2
            for v2 in range(v1 + 4, Candle.maxIndex(broker, symbol)):
                if cls.bearHG(broker, symbol, timeframe, v2):
                    if not Candle.breakOut(broker, symbol, timeframe, v2 - v1 - 1, v1):
                        return False
                    if not Candle.share(broker, symbol, timeframe, v1, v2):
                        return False
                    if min(Candle.bodySize(broker, symbol, timeframe, v1), Candle.bodySize(broker, symbol, timeframe, v2)) <= Candle.bigBody(broker, symbol, timeframe, v2 - v1 - 1, v1 + 1):
                        return False
                    if any([Candle.point(broker, symbol, timeframe, v1) < Candle.highest(broker, symbol, timeframe, 'close', v2 - v1 - 1, v1 + 1), Candle.point(broker, symbol, timeframe, v2) > Candle.lowest(broker, symbol, timeframe, 'close', v2 - v1 - 1, v1 + 1)]):
                        return False
                    return True
        return False

    @classmethod
    def bullStrongContinuation4(cls, broker, symbol, timeframe, v1):
        if cls.bullHG(broker, symbol, timeframe, v1):
            for v2 in range(v1 + 4, Candle.maxIndex(broker, symbol)):
                if cls.bullWRB(broker, symbol, timeframe, v2):
                    if not Candle.breakOut(broker, symbol, timeframe, v2 - v1 - 1, v1):
                        return False
                    if not Candle.share(broker, symbol, timeframe, v1, v2):
                        return False
                    if min(Candle.bodySize(broker, symbol, timeframe, v1), Candle.bodySize(broker, symbol, timeframe, v2)) <= Candle.bigBody(broker, symbol, timeframe, v2 - v1 - 1, v1 + 1):
                        return False
                    # Contraction volatility > body mid-point of V2
                    if not Candle.point(broker, symbol, timeframe, v2) < Candle.low(broker, symbol, timeframe, Candle.lowest(broker, symbol, timeframe, 'low', v2 - v1 - 1, v1 + 1)):
                        return False
                    # Body of V1 must be larger than the body of V2
                    if not Candle.bodySize(broker, symbol, timeframe, v1) <= Candle.bodySize(broker, symbol, timeframe, v2):
                        return False
                    return True
        return False

    @classmethod
    def bearStrongContinuation4(cls, broker, symbol, timeframe, v1):
        if cls.bearHG(broker, symbol, timeframe, v1):
            for v2 in range(v1 + 4, Candle.maxIndex(broker, symbol)):
                if cls.bearWRB(broker, symbol, timeframe, v2):
                    if not Candle.breakOut(broker, symbol, timeframe, v2 - v1 - 1, v1):
                        return False
                    if not Candle.share(broker, symbol, timeframe, v1, v2):
                        return False
                    if min(Candle.bodySize(broker, symbol, timeframe, v1), Candle.bodySize(broker, symbol, timeframe, v2)) <= Candle.bigBody(broker, symbol, timeframe, v2 - v1 - 1, v1 + 1):
                        return False
                    # Contraction volatility > body mid-point of V2
                    if not Candle.point(broker, symbol, timeframe, v2) > Candle.high(broker, symbol, timeframe, Candle.highest(broker, symbol, timeframe, 'high', v2 - v1 - 1, v1 + 1)):
                        return False
                    # Body of V1 must be larger than the body of V2
                    if not Candle.bodySize(broker, symbol, timeframe, v1) <= Candle.bodySize(broker, symbol, timeframe, v2):
                        return False
                    return True
        return False


class Confirmation(object):
    """docstring for Confirmation"""
    @classmethod
    def bearA(cls, broker, symbol, timeframe, no):
        if Candle.falling(broker, symbol, timeframe, no):
            if WRB.bullWRB(broker, symbol, timeframe, no + 2):
                if Candle.rising(broker, symbol, timeframe, no + 1) or Candle.equal(broker, symbol, timeframe, no + 1):
                    if Candle.close(broker, symbol, timeframe, no) < Candle.open(broker, symbol, timeframe, no + 1):
                        if Candle.close(broker, symbol, timeframe, no) < Candle.point(broker, symbol, timeframe, no + 2):
                            return True
        return False

    @classmethod
    def bullA(cls, broker, symbol, timeframe, no):
        if Candle.rising(broker, symbol, timeframe, no):
            if WRB.bearWRB(broker, symbol, timeframe, no + 2):
                if Candle.falling(broker, symbol, timeframe, no + 1) or Candle.equal(broker, symbol, timeframe, no + 1):
                    if Candle.close(broker, symbol, timeframe, no) > Candle.open(broker, symbol, timeframe, no + 1):
                        if Candle.close(broker, symbol, timeframe, no) > Candle.point(broker, symbol, timeframe, no + 2):
                            return True
        return False

    @classmethod
    def bearB(cls, broker, symbol, timeframe, no):
        if Candle.falling(broker, symbol, timeframe, no):
            if WRB.bullWRB(broker, symbol, timeframe, no):
                if Candle.rising(broker, symbol, timeframe, no + 2):
                    if Candle.high(broker, symbol, timeframe, no) > Candle.close(broker, symbol, timeframe, no + 1):
                        if Candle.open((broker), symbol, timeframe, no) > Candle.point(broker, symbol, timeframe, no + 1):
                            if Candle.close(broker, symbol, timeframe, no) < Candle.point(broker, symbol, timeframe, no + 1):
                                if Candle.close(broker, symbol, timeframe, no) > Candle.open(broker, symbol, timeframe, no + 1):
                                    if Candle.bodySize(broker, symbol, timeframe, no) > Candle.bigBody(broker, symbol, timeframe, 3, no + 1):
                                        return True
        return False

    @classmethod
    def bullB(cls, broker, symbol, timeframe, no):
        if Candle.rising(broker, symbol, timeframe, no):
            if WRB.bearWRB(broker, symbol, timeframe, no):
                if Candle.falling(broker, symbol, timeframe, no + 2):
                    if Candle.low(broker, symbol, timeframe, no) < Candle.close(broker, symbol, timeframe, no + 1):
                        if Candle.open((broker), symbol, timeframe, no) < Candle.point(broker, symbol, timeframe, no + 1):
                            if Candle.close(broker, symbol, timeframe, no) > Candle.point(broker, symbol, timeframe, no + 1):
                                if Candle.close(broker, symbol, timeframe, no) < Candle.open(broker, symbol, timeframe, no + 1):
                                    if Candle.bodySize(broker, symbol, timeframe, no) > Candle.bigBody(broker, symbol, timeframe, 3, no + 1):
                                        return True
        return False

    @classmethod
    def bearC(cls, broker, symbol, timeframe, no):
        if Candle.falling(broker, symbol, timeframe, no) and Candle.falling(broker, symbol, timeframe, no + 1):
            if WRB.bullWRB(broker, symbol, timeframe, no + 2):
                if Candle.close(broker, symbol, timeframe, no) < Candle.close(broker, symbol, timeframe, no + 1):
                    if Candle.high(broker, symbol, timeframe, no + 1) > Candle.close(broker, symbol, timeframe, no + 2):
                        if Candle.open(broker, symbol, timeframe, no + 1) <= Candle.close(broker, symbol, timeframe, no + 2):
                            if Candle.high(broker, symbol, timeframe, no) <= Candle.close(broker, symbol, timeframe, no + 2):
                                if Candle.close(broker, symbol, timeframe, no) >= Candle.open(broker, symbol, timeframe, no + 2):
                                    if Candle.low(broker, symbol, timeframe, no) <= Candle.point(broker, symbol, timeframe, no + 2):
                                        if len([x for x in [Candle.bodySize(broker, symbol, timeframe, no + 1) < x for x in [Candle.bodySize(broker, symbol, timeframe, x) for x in range(no + 3, no + 5)]] if x == True]) >= 2 or Candle.upShadowSize(broker, symbol, timeframe, no + 1) > Candle.bigBody(broker, symbol, timeframe, 3, no + 3):
                                            return True
        return False

    @classmethod
    def bullC(cls, broker, symbol, timeframe, no):
        if Candle.rising(broker, symbol, timeframe, no) and Candle.rising(broker, symbol, timeframe, no + 1):
            if WRB.bearWRB(broker, symbol, timeframe, no + 2):
                if Candle.close(broker, symbol, timeframe, no) > Candle.close(broker, symbol, timeframe, no + 1):
                    if Candle.low(broker, symbol, timeframe, no + 1) < Candle.close(broker, symbol, timeframe, no + 2):
                        if Candle.open(broker, symbol, timeframe, no + 1) >= Candle.close(broker, symbol, timeframe, no + 2):
                            if Candle.low(broker, symbol, timeframe, no) >= Candle.close(broker, symbol, timeframe, no + 2):
                                if Candle.close(broker, symbol, timeframe, no) <= Candle.open(broker, symbol, timeframe, no + 2):
                                    if Candle.high(broker, symbol, timeframe, no) >= Candle.point(broker, symbol, timeframe, no + 2):
                                        if len([x for x in [Candle.bodySize(broker, symbol, timeframe, no + 1) < x for x in [Candle.bodySize(broker, symbol, timeframe, x) for x in range(no + 3, no + 5)]] if x == True]) >= 2 or Candle.dnShadowSize(broker, symbol, timeframe, no + 1) > Candle.bigBody(broker, symbol, timeframe, 3, no + 3):
                                            return True
        return False

    @classmethod
    def bearD(cls, broker, symbol, timeframe, no):
        if Candle.withinRange(broker, symbol, timeframe, no, no + 1) or Candle.withinRange(broker, symbol, timeframe, no, no + 2):
            if Canlde.close(broker, symbol, timeframe, no) < max([Candle.close(broker, symbol, timeframe, no + 1), Candle.open(broker, symbol, timeframe, no + 1)]):
                if Candle.open(broker, symbol, timeframe, no) > max([Candle.close(broker, symbol, timeframe, no + 1), Candle.open(broker, symbol, timeframe, no + 1)]):
                    if WRB.bearWRB(broker, symbol, timeframe, no):
                        return True
                    else:
                        if max([Candle.close(broker, symbol, timeframe, no + 1), Candle.open(broker, symbol, timeframe, no + 1)]) > Candle.high(broker, symbol, timeframe, no + 2):
                            return True
        return False

    @classmethod
    def bullD(cls, broker, symbol, timeframe, no):
        if Candle.withinRange(broker, symbol, timeframe, no, no + 1) or Candle.withinRange(broker, symbol, timeframe, no, no + 2):
            if Canlde.close(broker, symbol, timeframe, no) > min([Candle.close(broker, symbol, timeframe, no + 1), Candle.open(broker, symbol, timeframe, no + 1)]):
                if Candle.open(broker, symbol, timeframe, no) < min([Candle.close(broker, symbol, timeframe, no + 1), Candle.open(broker, symbol, timeframe, no + 1)]):
                    if WRB.bullWRB(broker, symbol, timeframe, no):
                        return True
                    else:
                        if min([Candle.close(broker, symbol, timeframe, no + 1), Candle.open(broker, symbol, timeframe, no + 1)]) > Candle.low(broker, symbol, timeframe, no + 2):
                            return True
        return False

    @classmethod
    def bearE(cls, broker, symbol, timeframe, no):
        if Candle.open(broker, symbol, timeframe, no + 1) > Candle.close(broker, symbol, timeframe, no + 2):
            if Candle.close(broker, symbol, timeframe, no) < Candle.close(broker, symbol, timeframe, no + 1):
                if Candle.close(broker, symbol, timeframe, no) < Candle.open(broker, symbol, timeframe, no + 2):
                    if Candle.close(broker, symbol, timeframe, no + 2) > Candle.close(broker, symbol, timeframe, no + 3):
                        if Candle.close(broker, symbol, timeframe, no) > Candle.point(broker, symbol, timeframe, no + 3):
                            return True
        return False

    @classmethod
    def bullE(cls, broker, symbol, timeframe, no):
        if Candle.open(broker, symbol, timeframe, no + 1) < Candle.close(broker, symbol, timeframe, no + 2):
            if Candle.close(broker, symbol, timeframe, no) > Candle.close(broker, symbol, timeframe, no + 1):
                if Candle.close(broker, symbol, timeframe, no) > Candle.open(broker, symbol, timeframe, no + 2):
                    if Candle.close(broker, symbol, timeframe, no + 2) < Candle.close(broker, symbol, timeframe, no + 3):
                        if Candle.close(broker, symbol, timeframe, no) < Candle.point(broker, symbol, timeframe, no + 3):
                            return True
        return False

# @classmethod
# def bearF(cls, broker, symbol, timeframe, no):
#     if WRB.bearWRB(broker, symbol, timeframe, no):
#         for x in range(no + 2, no + 14):
#             if Candle.rising(broker, symbol, timeframe, x) and Candle.rising(broker, symbol, timeframe, x + 1):
#                 if Candle.longShadow(broker, symbol, timeframe, 'dn', x + 1):
#                     if Candle.withinRange(broker, symbol, timeframe, no, *args)


class Analyze(object):
    """docstring for Analyze"""
    @classmethod
    def run(self):
        t1 = datetime.datetime.now()
        for broker in Candle.db:
            for symbol in Candle.db[broker]:
                for row in Candle.db[broker][symbol]['quote']:
                    index = Candle.db[broker][symbol]['quote'].index(row)
                    if WRB.bullWRB(broker, symbol, 15, index):
                        WRB.db['WRB'][row[0]] = {'type': 'WRB', 'direction': 'bull'}
                    if WRB.bearWRB(broker, symbol, 15, index):
                        WRB.db['WRB'][row[0]] = {'type': 'WRB', 'direction': 'bear'}
                    if WRB.bullHG(broker, symbol, 15, index):
                        WRB.db['WRB'][row[0]] = {'type': 'HG', 'direction': 'bull'}
                    if WRB.bearHG(broker, symbol, 15, index):
                        WRB.db['WRB'][row[0]] = {'type': 'HG', 'direction': 'bear'}
                    # if WRB.bullSwingPoint1(broker, symbol, 1, index):
                    #     WRB.db['ZONE'][row[0]] = {'type': 'SP1', 'direction': 'bull'}
                    # if WRB.bearSwingPoint1(broker, symbol, 1, index):
                    #     WRB.db['ZONE'][row[0]] = {'type': 'SP1', 'direction': 'bear'}
                    # if WRB.bullSwingPoint2(broker, symbol, 1, index):
                    #     WRB.db['ZONE'][row[0]] = {'type': 'SP2', 'direction': 'bull'}
                    # if WRB.bearSwingPoint2(broker, symbol, 1, index):
                    #     WRB.db['ZONE'][row[0]] = {'type': 'SP2', 'direction': 'bear'}
                    # if WRB.bullStrongContinuation1(broker, symbol, 1, index):
                    #     WRB.db['ZONE'][row[0]] = {'type': 'SC1', 'direction': 'bull'}
                    # if WRB.bearStrongContinuation1(broker, symbol, 1, index):
                    #     WRB.db['ZONE'][row[0]] = {'type': 'SC1', 'direction': 'bear'}
                    # if WRB.bullStrongContinuation2(broker, symbol, 1, index):
                    #     WRB.db['ZONE'][row[0]] = {'type': 'SC2', 'direction': 'bull'}
                    # if WRB.bearStrongContinuation2(broker, symbol, 1, index):
                    #     WRB.db['WRB'][row[0]] = {'type': 'SC2', 'direction': 'bear'}
                    # if WRB.bullStrongContinuation3(broker, symbol, 1, index):
                    #     WRB.db['ZONE'][row[0]] = {'type': 'SC3', 'direction': 'bull'}
                    # if WRB.bearStrongContinuation3(broker, symbol, 1, index):
                    #     WRB.db['ZONE'][row[0]] = {'type': 'SC3', 'direction': 'bear'}
                    # if WRB.bullStrongContinuation4(broker, symbol, 1, index):
                    #     WRB.db['ZONE'][row[0]] = {'type': 'SC4', 'direction': 'bull'}
                    # if WRB.bearStrongContinuation4(broker, symbol, 1, index):
                    #     WRB.db['WRB'][row[0]] = {'type': 'SC4', 'direction': 'bear'}

                for signal in WRB.db:
                    with open('{0}_{1}_{2}_.csv'.format(broker, symbol, signal), mode='w') as f:
                        w = csv.writer(f, delimiter=';')
                        for date in sorted(WRB.db[signal]):
                            signal_type = WRB.db[signal][date]['type']
                            signal_direction = WRB.db[signal][date]['direction']
                            w.writerow([date, signal_type, signal_direction])


if __name__ == '__main__':

    from dukascopy import *
    downloadDukasData('EURUSD', 10000, 100000, False)
    Settings.load()
    Analyze.run()
