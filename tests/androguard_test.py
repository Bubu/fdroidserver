#!/usr/bin/env python3

import logging
import os

import testbase
import fdroidserver.common
import fdroidserver.metadata
import fdroidserver.update


class UpdateTest(testbase.TestBase):
    '''fdroid androguard manual tests'''

    def testScanMetadataAndroguardAAPT(self):

        def _create_apkmetadata_object(apkName):
            '''Create an empty apk metadata object'''
            apk = {}
            apk['apkName'] = apkName
            apk['uses-permission'] = []
            apk['uses-permission-sdk-23'] = []
            apk['features'] = []
            apk['icons_src'] = {}
            return apk

        config = dict()
        fdroidserver.common.fill_config_defaults(config)
        fdroidserver.update.config = config
        os.chdir(os.path.dirname(__file__))
        if os.path.basename(os.getcwd()) != 'tests':
            raise Exception('This test must be run in the "tests/" subdir')

        config['ndk_paths'] = dict()
        config['accepted_formats'] = ['json', 'txt', 'yml']
        fdroidserver.common.config = config
        fdroidserver.update.config = config

        fdroidserver.update.options = type('', (), {})()
        fdroidserver.update.options.clean = True
        fdroidserver.update.options.delete_unknown = True

        self.assertTrue(fdroidserver.common.SdkToolsPopen('aapt'))
        try:
            from androguard.core.bytecodes.apk import APK
            dir(APK)
        except ImportError:
            raise Exception("androguard not installed!")

        apkList = ['../info.guardianproject.urzip.apk', '../org.dyndns.fules.ck_20.apk']

        for apkName in apkList:
            logging.debug("Processing " + apkName)
            apkfile = os.path.join('repo', apkName)

            apkaapt = _create_apkmetadata_object(apkName)
            logging.debug("Using AAPT for metadata")
            fdroidserver.update.scan_apk_aapt(apkaapt, apkfile)
            # avoid AAPT application name bug
            del apkaapt['name']

            apkandroguard = _create_apkmetadata_object(apkName)
            logging.debug("Using androguard for metadata")
            fdroidserver.update.scan_apk_androguard(apkandroguard, apkfile)
            # avoid AAPT application name bug
            del apkandroguard['name']

            self.maxDiff = None
            self.assertEqual(apkaapt, apkandroguard)


if __name__ == "__main__":
    UpdateTest.main()
