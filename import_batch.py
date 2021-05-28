import os
import sys
import re
from neuroport_dbs.ImportNS5FeaturesGUI import NS5OfflinePlayback

PATH = "/tmp/data"
IGNORE = [
    '003', '007', '008', '009', '013', '015', '016', '018', '019', '022', '023', '024', '025', '027', '033', '034', '036', '037', '040'
]
def is_ns5_in_list(flist):
    for f in flist:
        if f.endswith('.ns5'):
            return True
    return False

def is_stn_case(case):
    return case not in IGNORE

if __name__ == "__main__":
    from qtpy.QtWidgets import QApplication
    qapp = QApplication(sys.argv)

    id_re = re.compile(r"(?P<Date>\d{4}[-_]?\d{2}[-_]?\d{2})[_-]+(?P<Id>\d+)[-_]?(?P<Proc>\d+).ns5")

    subj = {}
    for root, sub, flist in os.walk(PATH):

        case = os.path.split(root)[-1]

        if is_stn_case(case) and is_ns5_in_list(flist):

            if case not in list(subj.keys()):
                subj[case] = {}

            for f in flist:
                if f.endswith('.ns5'):

                    matches = id_re.match(f)
                    proc_id = matches.group('Id')
                    ch = matches.group('Proc')

                    if proc_id not in subj[case]:
                        subj[case][proc_id] = []
                    subj[case][proc_id] += [f]

    for case, procs in subj.items():
        for p, flist in procs.items():
            for fname in flist:
                fn, ext = os.path.splitext(fname)
                ch = fn.split('-')[-1]
                sub = f'{case}-{p}'.format(case, p)
                print(os.path.exists(os.path.join(PATH, case, fn+'.ns5')))
                NS5OfflinePlayback(sub, ch, os.path.join(PATH, case, fn))
#                try:
#                    NS5OfflinePlayback(sub, ch, os.path.join(PATH, case, fn))
#                    print(sub, ch, os.path.join(PATH, case, fn))
#                except:
#                    print(f"{sub}, {ch}", " ran into an error!")

