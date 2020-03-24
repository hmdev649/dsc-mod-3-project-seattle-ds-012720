"""
Thierry Bertin-Mahieux (2010) Columbia University
tb2332@columbia.edu


This code contains a set of getters functions to access the fields
from an HDF5 song file (regular file with one song or
aggregate / summary file with many songs)

This is part of the Million Song Dataset project from
LabROSA (Columbia University) and The Echo Nest.


Copyright 2010, Thierry Bertin-Mahieux

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import tables


def open_h5_file_read(h5filename):
    """
    Open an existing H5 in read mode.
    Same function as in hdf5_utils, here so we avoid one import
    """
    return tables.open_file(h5filename, mode='r')


def get_num_songs(h5):
    """
    Return the number of songs contained in this h5 file, i.e. the number of rows
    for all basic informations like name, artist, ...
    """
    return h5.root.metadata.songs.nrows

<<<<<<< HEAD

def get_artist_familiarity(h5, songidx=0):
=======
def get_artist_familiarity(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist familiarity from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_familiarity[songidx]

<<<<<<< HEAD

def get_artist_hotttnesss(h5, songidx=0):
=======
def get_artist_hotttnesss(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist hotttnesss from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_hotttnesss[songidx]

<<<<<<< HEAD

def get_artist_id(h5, songidx=0):
=======
def get_artist_id(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_id[songidx]

<<<<<<< HEAD

def get_artist_mbid(h5, songidx=0):
=======
def get_artist_mbid(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist musibrainz id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_mbid[songidx]

<<<<<<< HEAD

def get_artist_playmeid(h5, songidx=0):
=======
def get_artist_playmeid(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist playme id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_playmeid[songidx]

<<<<<<< HEAD

def get_artist_7digitalid(h5, songidx=0):
=======
def get_artist_7digitalid(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist 7digital id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_7digitalid[songidx]

<<<<<<< HEAD

def get_artist_latitude(h5, songidx=0):
=======
def get_artist_latitude(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist latitude from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_latitude[songidx]

<<<<<<< HEAD

def get_artist_longitude(h5, songidx=0):
=======
def get_artist_longitude(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist longitude from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_longitude[songidx]

<<<<<<< HEAD

def get_artist_location(h5, songidx=0):
=======
def get_artist_location(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist location from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_location[songidx]

<<<<<<< HEAD

def get_artist_name(h5, songidx=0):
=======
def get_artist_name(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist name from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.artist_name[songidx]

<<<<<<< HEAD

def get_release(h5, songidx=0):
=======
def get_release(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get release from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.release[songidx]

<<<<<<< HEAD

def get_release_7digitalid(h5, songidx=0):
=======
def get_release_7digitalid(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get release 7digital id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.release_7digitalid[songidx]

<<<<<<< HEAD

def get_song_id(h5, songidx=0):
=======
def get_song_id(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get song id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.song_id[songidx]

<<<<<<< HEAD

def get_song_hotttnesss(h5, songidx=0):
=======
def get_song_hotttnesss(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get song hotttnesss from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.song_hotttnesss[songidx]

<<<<<<< HEAD

def get_title(h5, songidx=0):
=======
def get_title(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get title from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.title[songidx]

<<<<<<< HEAD

def get_track_7digitalid(h5, songidx=0):
=======
def get_track_7digitalid(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get track 7digital id from a HDF5 song file, by default the first song in it
    """
    return h5.root.metadata.songs.cols.track_7digitalid[songidx]

<<<<<<< HEAD

def get_similar_artists(h5, songidx=0):
=======
def get_similar_artists(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get similar artists array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.metadata.songs.nrows == songidx + 1:
        return h5.root.metadata.similar_artists[h5.root.metadata.songs.cols.idx_similar_artists[songidx]:]
    return h5.root.metadata.similar_artists[h5.root.metadata.songs.cols.idx_similar_artists[songidx]:
                                            h5.root.metadata.songs.cols.idx_similar_artists[songidx+1]]

<<<<<<< HEAD

def get_artist_terms(h5, songidx=0):
=======
def get_artist_terms(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist terms array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.metadata.songs.nrows == songidx + 1:
        return h5.root.metadata.artist_terms[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
    return h5.root.metadata.artist_terms[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
<<<<<<< HEAD
                                         h5.root.metadata.songs.cols.idx_artist_terms[songidx+1]]


def get_artist_terms_freq(h5, songidx=0):
=======
                                            h5.root.metadata.songs.cols.idx_artist_terms[songidx+1]]

def get_artist_terms_freq(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.metadata.songs.nrows == songidx + 1:
        return h5.root.metadata.artist_terms_freq[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
    return h5.root.metadata.artist_terms_freq[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                              h5.root.metadata.songs.cols.idx_artist_terms[songidx+1]]

<<<<<<< HEAD

def get_artist_terms_weight(h5, songidx=0):
=======
def get_artist_terms_weight(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.metadata.songs.nrows == songidx + 1:
        return h5.root.metadata.artist_terms_weight[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
    return h5.root.metadata.artist_terms_weight[h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                                h5.root.metadata.songs.cols.idx_artist_terms[songidx+1]]

<<<<<<< HEAD

def get_analysis_sample_rate(h5, songidx=0):
=======
def get_analysis_sample_rate(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get analysis sample rate from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.analysis_sample_rate[songidx]

<<<<<<< HEAD

def get_audio_md5(h5, songidx=0):
=======
def get_audio_md5(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get audio MD5 from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.audio_md5[songidx]

<<<<<<< HEAD

def get_danceability(h5, songidx=0):
=======
def get_danceability(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get danceability from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.danceability[songidx]

<<<<<<< HEAD

def get_duration(h5, songidx=0):
=======
def get_duration(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get duration from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.duration[songidx]

<<<<<<< HEAD

def get_end_of_fade_in(h5, songidx=0):
=======
def get_end_of_fade_in(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get end of fade in from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.end_of_fade_in[songidx]

<<<<<<< HEAD

def get_energy(h5, songidx=0):
=======
def get_energy(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get energy from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.energy[songidx]

<<<<<<< HEAD

def get_key(h5, songidx=0):
=======
def get_key(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get key from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.key[songidx]

<<<<<<< HEAD

def get_key_confidence(h5, songidx=0):
=======
def get_key_confidence(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get key confidence from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.key_confidence[songidx]

<<<<<<< HEAD

def get_loudness(h5, songidx=0):
=======
def get_loudness(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get loudness from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.loudness[songidx]

<<<<<<< HEAD

def get_mode(h5, songidx=0):
=======
def get_mode(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get mode from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.mode[songidx]

<<<<<<< HEAD

def get_mode_confidence(h5, songidx=0):
=======
def get_mode_confidence(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get mode confidence from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.mode_confidence[songidx]

<<<<<<< HEAD

def get_start_of_fade_out(h5, songidx=0):
=======
def get_start_of_fade_out(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get start of fade out from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.start_of_fade_out[songidx]

<<<<<<< HEAD

def get_tempo(h5, songidx=0):
=======
def get_tempo(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get tempo from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.tempo[songidx]

<<<<<<< HEAD

def get_time_signature(h5, songidx=0):
=======
def get_time_signature(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get signature from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.time_signature[songidx]

<<<<<<< HEAD

def get_time_signature_confidence(h5, songidx=0):
=======
def get_time_signature_confidence(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get signature confidence from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.time_signature_confidence[songidx]

<<<<<<< HEAD

def get_track_id(h5, songidx=0):
=======
def get_track_id(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get track id from a HDF5 song file, by default the first song in it
    """
    return h5.root.analysis.songs.cols.track_id[songidx]

<<<<<<< HEAD

def get_segments_start(h5, songidx=0):
=======
def get_segments_start(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get segments start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_start[h5.root.analysis.songs.cols.idx_segments_start[songidx]:]
    return h5.root.analysis.segments_start[h5.root.analysis.songs.cols.idx_segments_start[songidx]:
                                           h5.root.analysis.songs.cols.idx_segments_start[songidx+1]]
<<<<<<< HEAD


def get_segments_confidence(h5, songidx=0):
=======
    
def get_segments_confidence(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get segments confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_confidence[h5.root.analysis.songs.cols.idx_segments_confidence[songidx]:]
    return h5.root.analysis.segments_confidence[h5.root.analysis.songs.cols.idx_segments_confidence[songidx]:
                                                h5.root.analysis.songs.cols.idx_segments_confidence[songidx+1]]

<<<<<<< HEAD

def get_segments_pitches(h5, songidx=0):
=======
def get_segments_pitches(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get segments pitches array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
<<<<<<< HEAD
        return h5.root.analysis.segments_pitches[h5.root.analysis.songs.cols.idx_segments_pitches[songidx]:, :]
    return h5.root.analysis.segments_pitches[h5.root.analysis.songs.cols.idx_segments_pitches[songidx]:
                                             h5.root.analysis.songs.cols.idx_segments_pitches[songidx+1], :]


def get_segments_timbre(h5, songidx=0):
=======
        return h5.root.analysis.segments_pitches[h5.root.analysis.songs.cols.idx_segments_pitches[songidx]:,:]
    return h5.root.analysis.segments_pitches[h5.root.analysis.songs.cols.idx_segments_pitches[songidx]:
                                             h5.root.analysis.songs.cols.idx_segments_pitches[songidx+1],:]

def get_segments_timbre(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get segments timbre array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
<<<<<<< HEAD
        return h5.root.analysis.segments_timbre[h5.root.analysis.songs.cols.idx_segments_timbre[songidx]:, :]
    return h5.root.analysis.segments_timbre[h5.root.analysis.songs.cols.idx_segments_timbre[songidx]:
                                            h5.root.analysis.songs.cols.idx_segments_timbre[songidx+1], :]


def get_segments_loudness_max(h5, songidx=0):
=======
        return h5.root.analysis.segments_timbre[h5.root.analysis.songs.cols.idx_segments_timbre[songidx]:,:]
    return h5.root.analysis.segments_timbre[h5.root.analysis.songs.cols.idx_segments_timbre[songidx]:
                                            h5.root.analysis.songs.cols.idx_segments_timbre[songidx+1],:]

def get_segments_loudness_max(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get segments loudness max array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_loudness_max[h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx]:]
    return h5.root.analysis.segments_loudness_max[h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx]:
                                                  h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx+1]]

<<<<<<< HEAD

def get_segments_loudness_max_time(h5, songidx=0):
=======
def get_segments_loudness_max_time(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get segments loudness max time array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_loudness_max_time[h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx]:]
    return h5.root.analysis.segments_loudness_max_time[h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx]:
                                                       h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx+1]]

<<<<<<< HEAD

def get_segments_loudness_start(h5, songidx=0):
=======
def get_segments_loudness_start(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get segments loudness start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.segments_loudness_start[h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx]:]
    return h5.root.analysis.segments_loudness_start[h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx]:
                                                    h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx+1]]

<<<<<<< HEAD

def get_sections_start(h5, songidx=0):
=======
def get_sections_start(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get sections start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.sections_start[h5.root.analysis.songs.cols.idx_sections_start[songidx]:]
    return h5.root.analysis.sections_start[h5.root.analysis.songs.cols.idx_sections_start[songidx]:
                                           h5.root.analysis.songs.cols.idx_sections_start[songidx+1]]

<<<<<<< HEAD

def get_sections_confidence(h5, songidx=0):
=======
def get_sections_confidence(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get sections confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.sections_confidence[h5.root.analysis.songs.cols.idx_sections_confidence[songidx]:]
    return h5.root.analysis.sections_confidence[h5.root.analysis.songs.cols.idx_sections_confidence[songidx]:
                                                h5.root.analysis.songs.cols.idx_sections_confidence[songidx+1]]

<<<<<<< HEAD

def get_beats_start(h5, songidx=0):
=======
def get_beats_start(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get beats start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.beats_start[h5.root.analysis.songs.cols.idx_beats_start[songidx]:]
    return h5.root.analysis.beats_start[h5.root.analysis.songs.cols.idx_beats_start[songidx]:
                                        h5.root.analysis.songs.cols.idx_beats_start[songidx+1]]

<<<<<<< HEAD

def get_beats_confidence(h5, songidx=0):
=======
def get_beats_confidence(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get beats confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.beats_confidence[h5.root.analysis.songs.cols.idx_beats_confidence[songidx]:]
    return h5.root.analysis.beats_confidence[h5.root.analysis.songs.cols.idx_beats_confidence[songidx]:
                                             h5.root.analysis.songs.cols.idx_beats_confidence[songidx+1]]

<<<<<<< HEAD

def get_bars_start(h5, songidx=0):
=======
def get_bars_start(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get bars start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.bars_start[h5.root.analysis.songs.cols.idx_bars_start[songidx]:]
    return h5.root.analysis.bars_start[h5.root.analysis.songs.cols.idx_bars_start[songidx]:
                                       h5.root.analysis.songs.cols.idx_bars_start[songidx+1]]

<<<<<<< HEAD

def get_bars_confidence(h5, songidx=0):
=======
def get_bars_confidence(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get bars start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.bars_confidence[h5.root.analysis.songs.cols.idx_bars_confidence[songidx]:]
    return h5.root.analysis.bars_confidence[h5.root.analysis.songs.cols.idx_bars_confidence[songidx]:
                                            h5.root.analysis.songs.cols.idx_bars_confidence[songidx+1]]

<<<<<<< HEAD

def get_tatums_start(h5, songidx=0):
=======
def get_tatums_start(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get tatums start array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.tatums_start[h5.root.analysis.songs.cols.idx_tatums_start[songidx]:]
    return h5.root.analysis.tatums_start[h5.root.analysis.songs.cols.idx_tatums_start[songidx]:
                                         h5.root.analysis.songs.cols.idx_tatums_start[songidx+1]]

<<<<<<< HEAD

def get_tatums_confidence(h5, songidx=0):
=======
def get_tatums_confidence(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get tatums confidence array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.analysis.songs.nrows == songidx + 1:
        return h5.root.analysis.tatums_confidence[h5.root.analysis.songs.cols.idx_tatums_confidence[songidx]:]
    return h5.root.analysis.tatums_confidence[h5.root.analysis.songs.cols.idx_tatums_confidence[songidx]:
                                              h5.root.analysis.songs.cols.idx_tatums_confidence[songidx+1]]

<<<<<<< HEAD

def get_artist_mbtags(h5, songidx=0):
=======
def get_artist_mbtags(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist musicbrainz tag array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.musicbrainz.songs.nrows == songidx + 1:
        return h5.root.musicbrainz.artist_mbtags[h5.root.musicbrainz.songs.cols.idx_artist_mbtags[songidx]:]
    return h5.root.musicbrainz.artist_mbtags[h5.root.metadata.songs.cols.idx_artist_mbtags[songidx]:
                                             h5.root.metadata.songs.cols.idx_artist_mbtags[songidx+1]]

<<<<<<< HEAD

def get_artist_mbtags_count(h5, songidx=0):
=======
def get_artist_mbtags_count(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get artist musicbrainz tag count array. Takes care of the proper indexing if we are in aggregate
    file. By default, return the array for the first song in the h5 file.
    To get a regular numpy ndarray, cast the result to: numpy.array( )
    """
    if h5.root.musicbrainz.songs.nrows == songidx + 1:
        return h5.root.musicbrainz.artist_mbtags_count[h5.root.musicbrainz.songs.cols.idx_artist_mbtags[songidx]:]
    return h5.root.musicbrainz.artist_mbtags_count[h5.root.metadata.songs.cols.idx_artist_mbtags[songidx]:
                                                   h5.root.metadata.songs.cols.idx_artist_mbtags[songidx+1]]

<<<<<<< HEAD

def get_year(h5, songidx=0):
=======
def get_year(h5,songidx=0):
>>>>>>> 396bcec7743f5140581d2244aeecb87af01f3b6a
    """
    Get release year from a HDF5 song file, by default the first song in it
    """
    return h5.root.musicbrainz.songs.cols.year[songidx]
