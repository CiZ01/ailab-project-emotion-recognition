from torch.utils.data import Dataset
import glob
from PIL import Image
import numpy as np
    
class FERDataset(Dataset):
    '''
    
    '''
    def __init__(self, dataset_path, transform=None):
        '''
        dataset_path: the parent directory of train and test
        trasform: torchvision.transforms

        '''
        assert dataset_path.split('/')[-1] in {'train', 'test'}, 'dataset_path should be the parent directory of train and test'
        
        self.image_paths = glob.glob(f'{dataset_path}/*/*.jpg')
        self.labels = {k.split('/')[-1]:v for (v,k) in enumerate(glob.glob(f'{dataset_path}/*'))}
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, index):
        if isinstance(index, tuple):
            sub_labels = index[-1]
            return [(np.asarray(Image.open(img)) / 255.0, self.labels[img.split('/')[-2]]) for img in self.image_paths[index[0]] if img.split('/')[-2] in sub_labels]
        
        if isinstance(index, slice):
            return [(np.asarray(Image.open(img)) / 255.0, self.labels[img.split('/')[-2]]) for img in self.image_paths[index]]
        

        # Open image and convert to numpy array, then normalize to [0, 1].
        image = np.asarray(Image.open(self.image_paths[index])) / 255.0
        label = self.labels[self.image_paths[index].split('/')[-2]]
        
        if self.transform is not None:
            image = self.transform(image)

        return image, label

if __name__ == '__main__':
    dataset = FERDataset('./dataset/test')
    print(len(dataset))
    print(dataset[0][0].shape)
