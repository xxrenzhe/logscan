from distutils.core import setup

setup( 
    name = "logscan", 
    version = "0.2.1", 
    author = "Thomas Leichtfuss", 
    author_email = "thomaslfuss@gmx.de",
    description = 'Command-line-tool to get time-specific access to log-files.'
    long_description = "This is a command-line-tool to get time-specific access to log-files, while rotated logfiles that are counted up (e.g. logfile.log, logfile.log.1, logfile.log.2.gz ...) are automatically taken together -also gzipped files are processed. Different date-time-formats are supported, inclusive simple timestamps as a huge number of seconds with three decimal-places, e.g. 123456789.123. Individual formats can be specified.",
    py_modules = ["logscanlib", "timeparse"],
    package_dir = {'' : 'src'},
    scripts = ["src/logscan"],
    data_files = [('etc', ['src/logscan.conf'])],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        'Topic :: System :: Logging',
    ],
    license='GPL',
    keywords='logfile logfiles log time-specific access rotated scan',
    entry_points={'console_scripts': ['logscan = logscan:main', ]},
)
