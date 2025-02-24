
general = {
    'comment': '',
    'baseline': 'toy.synthesis/lda.gensim.dynaernn',
    'cuda': '-1'
}
dal = {
    'path': '../data/toy.synthetic',
    'userModeling': True,#if true, timeModeling must be true also
    'timeModeling': True,
    'start': '2010-12-01',
    'end': '2010-12-04',
    'timeInterval': 1,  # unit of day
    'tagMe': False
}
tml = {
    'path2save': f'../output/{general["baseline"]}/tml',
    'numTopics': 3,
    'malletHome': 'C:/Users/Soroush/Desktop/mallet-2.0.8/mallet-2.0.8',
    'filterExtremes': False,
    'justOne': False,
    'binary': False,
    'threshold': 0.5,
    'method': 'lda.gensim' #['lda.gensim', 'lda.mallet', 'gsdmm']
}
uml = {
    'userSimilarityThreshold': 0.2,
    'path2save': f'../output/{general["baseline"]}/uml'
}
gel = {
    'path2save': f'../output/{general["baseline"]}/gel',
    'embeddingDim': 32,
    'epoch': 100,
    'method': 'dynaernn' #one of ['AE', 'DynAE', 'DynRNN', 'DynAERNN']
}
cpl = {
    'path2save': f'../output/{general["baseline"]}/cpl',
    'method': 'louvain',
    'minSize': 10
}
evl = {
    'evaluationType': 'Extrinsic',  # ['Intrinsic', 'Extrinsic']
    # If Extrinsic evaluation:
    'extrinsicEvaluationMetrics': {'success_1', 'success_5', 'success_10', 'success_100'},
    # If intrinsic evaluation:
    'intrinsicEvaluationMetrics': ['adjusted_rand', 'completeness', 'homogeneity', 'rand', 'v_measure', 'normalized_mutual_info', 'adjusted_mutual_info', 'mutual_info', 'fowlkes_mallows'],
    'goldenStandardPath': '/path2GS',
    'threshold': 0,


}

apl = {
    'path2save': f'../output/{general["baseline"]}/apl',
    'topK': 20,
    'textTitle': 'Text'
}