'''
File to import matchers. The module's import are within the functions, so that
a module is imported only iff needed, reducing the number of raised errors and
warnings due to unused modules.
'''


def get_matcher(matcher_name='sift-lg', device='cpu', max_num_keypoints=2048, *args, **kwargs):
    
    if matcher_name == 'loftr':
        from matching import loftr
        return loftr.LoftrMatcher(device, *args, **kwargs)
    
    elif matcher_name == 'sift-lg':
        from matching import lightglue
        return lightglue.SiftLightGlue(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'superpoint-lg':
        from matching import lightglue
        return lightglue.SuperpoingLightGlue(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'disk-lg':
        from matching import lightglue
        return lightglue.DiskLightGlue(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'aliked-lg':
        from matching import lightglue
        return lightglue.AlikedLightGlue(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'doghardnet-lg':
        from matching import lightglue
        return lightglue.DognetLightGlue(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'roma':
        from matching import roma
        return roma.RomaMatcher(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'dedode':
        from matching import dedode
        return dedode.DedodeMatcher(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'steerers':
        from matching import steerers
        return steerers.SteererMatcher(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'sift-nn':
        from matching import handcrafted
        return handcrafted.SiftNNMatcher(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'orb-nn':
        from matching import handcrafted
        return handcrafted.OrbNNMatcher(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'patch2pix':
        from matching import matching_toolbox
        return matching_toolbox.Patch2pixMatcher(device,*args, **kwargs)
    
    elif matcher_name == 'patch2pix_superglue':
        from matching import matching_toolbox
        return matching_toolbox.SuperGluePatch2pixMatcher(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'superglue':
        from matching import matching_toolbox
        return matching_toolbox.SuperGlueMatcher(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'r2d2':
        from matching import matching_toolbox
        return matching_toolbox.R2D2Matcher(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'd2net':
        from matching import matching_toolbox
        return matching_toolbox.D2netMatcher(device,*args, **kwargs)
    
    elif matcher_name == 'duster':
        from matching import duster
        return duster.DusterMatcher(device, max_num_keypoints,*args, **kwargs)
    
    elif matcher_name == 'doghardnet-nn':
        from matching import matching_toolbox
        return matching_toolbox.DogAffHardNNMatcher(device,*args, **kwargs)
    
    elif matcher_name == 'xfeat':
        from matching import xfeat
        return xfeat.xFeatMatcher(device, *args, **kwargs)
    
    else:
        raise RuntimeError(f'Matcher {matcher_name} does not exist')
