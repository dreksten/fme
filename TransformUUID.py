class TransformUuid():
    """
    Contains static methods for transforming UUID strings between their
    Oracle RAW and ISO equivalents.
    
     >>> TransformUuid.IsoToOra("066c16f2-9be4-6d47-b5f7-db6d9e8a13e6")
    'F2166C06E49B476DB5F7DB6D9E8A13E6'
    >>> TransformUuid.OraToIso("F2166C06E49B476DB5F7DB6D9E8A13E6", prefix="GUID:")
    'GUID:066c16f2-9be4-6d47-b5f7-db6d9e8a13e6'
    >>> TransformUuid.OraToIso("F2166C06E49B476DB5F7DB6D9E8A13E6")
    '066c16f2-9be4-6d47-b5f7-db6d9e8a13e6'
    """
    
    @staticmethod
    def IsoToOra(IsoUuid, prefix=""):
        uuid = IsoUuid.upper().strip().replace("-", "").replace(prefix, "")
        if len(uuid) != 32:
            raise ValueError("Invalid ISO UUID, expected 32 characters, received %d: %s" % (len(uuid), str(uuid)))

        oraUuid = uuid[6:8] + uuid[4:6] + uuid[2:4] + uuid[0:2] + uuid[10:12] + \
                  uuid[8:10] + uuid[14:16] + uuid[12:14] + uuid[16:21] + uuid[-11:]
        return oraUuid
    
    @staticmethod
    def OraToIso(OraUuid, prefix=""):
        uuid = OraUuid.lower().strip().replace("-", "").replace(prefix, "")
        if len(uuid) != 32:
            raise ValueError("Invalid Oracle UUID, expected 32 characters, received %d: %s" % (len(uuid), str(uuid)))

        isoUuid = uuid[6:8] + uuid[4:6] + uuid[2:4] + uuid[0:2] + uuid[10:12] + \
                  uuid[8:10] + uuid[14:16] + uuid[12:14] + uuid[16:21] + uuid[-11:]
        return TransformUuid.formatUuid(isoUuid, prefix)

    @staticmethod
    def formatUuid(uuid, prefix=""):
        if len(uuid) != 32:
            raise ValueError("Invalid UUID, expected 32 characters, received %d." % len(uuid))
        return "%s%s-%s-%s-%s-%s" % (prefix, uuid[:8], uuid[8:12], uuid[12:16], uuid[16:20], uuid[20:32])