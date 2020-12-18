import torch
import torch.nn as nn
import math

class SRNet(nn.Module):

	def __init__(self):
		super(SRNet, self).__init__()

		self.relu = nn.ReLU(inplace=True)
		self.pad = nn.ReflectionPad2d(1)

		self.Conv1 = nn.Conv2d(3,64,3,1,1,bias=True)
		self.Conv1_ = nn.Conv2d(3,64,5,1,1,bias=True)
		self.Conv2 = nn.Conv2d(128,64,3,1,1,bias=True)
		self.Conv3 = nn.Conv2d(64,64,3,1,1,bias=True)
		self.Conv4 = nn.Conv2d(64,3,3,1,1,bias=True)
		self.Conv5 = nn.Conv2d(3,64,3,1,1,bias=True)
		self.Conv6 = nn.Conv2d(64,64,3,1,1,bias=True)
		self.Conv7 = nn.Conv2d(64,64,3,1,1,bias=True)
		self.Conv8 = nn.Conv2d(64,3,3,1,1,bias=True)

	def forward(self, LR_img):

		x = self.relu(self.Conv1(LR_img))
		x_ = self.relu(self.Conv1_(self.pad(LR_img)))
		x = torch.cat((x,x_), dim=1)
		x = self.relu(self.Conv2(x))
		x = self.relu(self.Conv3(x))
		x = self.relu(self.Conv4(x))
		x = x + LR_img
		x = self.relu(self.Conv5(x))
		x = self.relu(self.Conv6(x))
		x = self.relu(self.Conv7(x))
		x = self.Conv8(x)

		SR_img = LR_img + x     # Because we have to learn residuals.

		return SR_img

