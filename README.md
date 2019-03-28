# StackGAN_WGAN_pytorch
Replace StackGAN's loss function with WGAN's loss function.

将StackGAN的loss函数替换为WGAN的loss函数

## Requirements

- `Python2`
- `pytorch==0.3.0` 
- `tensorboard`
- `python-dateutil`
- `easydict`
- `pandas`
- `torchfile`

## Model

模型基于StackGAN和WGAN，做了一些修改。以StackGAN为base model，将StackGAN的loss改为Wassertein loss，用来改善收敛速度，使得lossD和lossG表现更好。
实验结果证明，修改之后的模型在我们自己的数据集上收敛速度极大提高，并且之前一直降不下去的lossG下降到一个正常值，lossD也稳定在正常值，生成效果相比之前结果得到了提高。

程序运行请参考 https://github.com/hanzhanggit/StackGAN-Pytorch 中的运行方法

The model is based on StackGAN and WGAN, and we made some modifications.We use StackGAN as base model and change StackGAN loss into Wassertein loss,

## References

-[StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks](https://arxiv.org/pdf/1612.03242v2.pdf)

-[Wasserstein GAN](https://arxiv.org/abs/1701.07875)

-[令人拍案叫绝的Wasserstein GAN]https://zhuanlan.zhihu.com/p/25071913
