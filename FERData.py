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
        self.labels = [p.split('/')[-1] for p in glob.glob(f'{dataset_path}/*')]     
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, index):
        image = np.asarray(Image.open(self.image_paths[index]))
        label = self.image_paths[index].split('/')[-2]
        
        if self.transform is not None:
            image = self.transform(image)

        return image, label
    
if __name__ == '__main__':
    dataset = FERDataset('./dataset/train')
    print(dataset[0])
