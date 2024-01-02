import os
import re

ad_filters = [
    # Beginning of Ad Filters
    'Please rate this subtitle at www'
    'www.osdb.link',
    'Downloaded from',
    'api.OpenSubtitles.org is deprecated, please',
    'implement REST API from OpenSubtitles.com',
    'Support us and become a VIP member',
    'Support us and become VIP member',
    'to remove all ads from www.OpenSubtitles.org',
    'subtitles',
    'contact www.OpenSubtitles.org today',
    'corrected by',
    'corrections by',
    'Help other users to choose the best',
    'rate this subtitle',
    'Help other users to choose the best subtitles',
    'Please rate this subtitle at',
    'rate this subtitle',
    'Someone needs to stop Clearway Law. Public shouldnt leave reviews for lawyers.',
    'Advertise your product or brand here',
    'tvsubtitles',
    'YTS',
    'YIFY',
    'www\\.',
    'https:',
    'ripped by',
    'opensubtitles',
    'sub(scene|rip)',
    'podnapisi',
    'addic7ed',
    'titlovi',
    'bozxphd',
    'sazu489',
    'Do you want subtitles for any video?',
    '- =[ ai.OpenSubtitles.com ]=-',
    '- == [ www.OpenSubtitles.com ] ==-',
    '- == [ www.OpenSubtitles.org ] ==-',
    'psagmeno',
    'normita',
    'anoxmous',
    'ENJOY ALL VOD IN HIGH QUALITY @ 4KVOD.TV',
    'GET LIVE TV,MOVIES, SHOWS IN ONE PACKAGE',
    '©',
    '™',
    'Free Online Movies',
    'Subtitle edited by',
    # End of Ad Filters
]

def apply_changes(root_folder):
    changes_log = []
    movies_processed = 0

    for root, dirs, files in os.walk(root_folder):
        # Scan folders by Letter to break the operation into chunks
        dirs[:] = [d for d in dirs if 'A' <= d[0] <= 'A']
        
        for file in files:
            if file.endswith('.srt'):
                subtitle_path = os.path.join(root, file)
                movies_processed += 1

                with open(subtitle_path, 'r', encoding='utf-8', errors='ignore') as f:
                    file_lines = f.readlines()
                    changes_detected = False

                    for i, line in enumerate(file_lines):
                        for ad in ad_filters:
                            ad_pattern = re.escape(ad) + r'(?:\s+\S{5})?$'
                            if re.search(ad_pattern, line):
                                changes_detected = True
                                file_lines[i] = re.sub(ad_pattern, '', line)
                                
                        # Remove www.osdb.link/ completely
                        line = re.sub(r'www\.osdb\.link\/\w{5}', '', line)

                    if changes_detected:
                        with open(subtitle_path, 'w', encoding='utf-8') as file:
                            file.write(''.join(file_lines))
                            changes_log.append(f"Changes made to file: {subtitle_path}\n")

    with open('changelog.txt', 'w', encoding='utf-8') as changelog_file:
        changelog_file.write("Changes Log:\n\n")
        changelog_file.writelines(changes_log)

# Change 'Y:\\Movies' to your movie dir
apply_changes('Y:\\Movies')