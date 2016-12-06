###
# Copyright (c) 2016, Mike Burns
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('BHJF')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class BHJF(callbacks.Plugin):
    """brown hat jellyfish"""
    pass

    def bhjf(self, irc, msg, args):
        """ print the bhjf"""
        irc.reply(ircutils.mircColor('    ,~"""~.         ', fg='brown',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor(" ,-/       \-.      ", fg='brown',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("' '`._____.'` `.    ", fg='brown',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("-._         _,-'    ", fg='brown',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("   `--...--'        ", fg='brown',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("   .-;':':'-.       ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("  {'.'.'.'.'.}      ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("   )        '`.     ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("  '-. ._ ,_.-='     ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("    `). ( `);(      ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("    ('. .)(,'.)     ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("     ) ( ,').(      ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("    ( .').'(').     ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("    .) (' ).('      ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("     '  ) (  ).     ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("      .'( .)'       ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("        .).'        ", fg='black',
            bg='light blue'), prefixNick=False)
    bhjf = wrap(bhjf, [])

Class = BHJF


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
