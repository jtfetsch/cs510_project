import torch
from model import EncoderRNN

model_param_path = "model_parameters/crmodel.pt"


def main():
    hidden_size = 100
    encoder = EncoderRNN(hidden_size)
    encoder.load_state_dict(torch.load(model_param_path))

    
    


if __name__ == '__main__':
    main()
