from torchvision import models
from torchvision.models.resnet import ResNet101_Weights
from labels import labels
import torch
from torchvision import transforms
from PIL import Image

transform = transforms.Compose([           
 transforms.Resize(256),                 
 transforms.CenterCrop(224),             
 transforms.ToTensor(),                   
 transforms.Normalize(                    
 mean=[0.485, 0.456, 0.406],               
 std=[0.229, 0.224, 0.225]                 
 )])

img = Image.open("vending_machine.jpg")
img_t = transform(img)
batch_t = torch.unsqueeze(img_t, 0)

resnet = models.resnet101(weights=ResNet101_Weights.DEFAULT)
resnet.eval()
out = resnet(batch_t)

_, indices = torch.sort(out, descending=True)

percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

for idx in indices[0][:10]:
    print(idx)
    label = labels.get(int(idx.item()))
    print(label, percentage[idx].item()) 