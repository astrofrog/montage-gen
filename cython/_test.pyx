# http://docs.cython.org/src/userguide/external_C_code.html

cimport wrappers

a = 1

#
# cdef class MontageStruct:
#
#     cdef:
#         wrappers.mImgtblReturn *ret
#
#     cdef public:
#         int status;
#         int count;
#         int badfits;
#         int badwcs;
#
#     def __cinit__(self):
#         cdef char *pathnamein='.'
#         cdef char *tblname='images.tbl'
#         self.ret = wrappers.mImgtbl(pathnamein, tblname, 0, 0, 0, 0, 0, 0, '', '', 0)
        # self.status = self.ret.status
        # self.count = self.ret.count
        # self.badfits = self.ret.badfits
        # self.badwcs = self.ret.badwcs

# cdef class MontageStruct2:
#
#     cdef:
#         wrappers.mImgtblReturn *ret
#
#     cdef public:
#         int status;
#
#     def __cinit__(self, wrappers.mImgtblReturn ret):
#         self.status = ret.status

# {"type"="integer",                   "name"="count",            "desc"="Number of images found with valid headers (may be more than one per file)."},
# {"type"="integer",                   "name"="badfits",          "desc"="Number of bad FITS files."},
# {"type"="integer",                   "name"="badwcs",           "desc"="Number of images rejected because of bad WCS information."}

cdef test(char *pathnamein, char *tblname):
    cdef wrappers.mImgtblReturn *ret
    ret = wrappers.mImgtbl(pathnamein, tblname, 0, 0, 0, 0, 0, 0, '', '', 0)
    return {'status': ret.status, 'count': ret.count, 'badfits': ret.badfits, 'badwcs': ret.badwcs}

def testing():
    return test('.', 'images_test.tbl')
    # return MontageStruct()
    
    # cdef char *pathnamein='.'
    # cdef char *tblname='images.tbl'
    # cdef MontageStruct result = wrappers.mImgtbl(pathnamein, tblname, 0, 0, 0, 0, 0, 0, '', '', 0)[]
    
        
