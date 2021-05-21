class Net(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Net, self).__init__()
        self.hidden_size = hidden_size
        self.input_size = input_size
        self.output_size = output_size
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # Follow these steps:
        #
        # Flatten the input x keeping the batch dimension the same
        # Use the relu activation on the output of self.fc1(x)
        # Use the relu activation on the output of self.fc2(x)
        # Pass x through fc3 but do not apply any activation function (think why not?)
        
        
        # YOUR CODE HERE (please remove 'raise NotImplementedError()')
        #print(self.input_size)
        #print(x.shape)
        x = x.view(-1, self.input_size)
        #print(x.shape)
        x = F.relu(self.fc1(x))
        #print(x.shape)
        x = F.relu(self.fc2(x))
        #print(x.shape)
        x = self.fc3(x)
        #print(x.shape)
        
        return x  # Return x (logits)