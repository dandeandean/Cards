package util

import (
	"os"

	"sigs.k8s.io/yaml"
)

type Config struct {
	DataPath string `json:"path"`
}

func ConfigFromFile(path string) Config {
	data, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}
	config := &Config{}
	err = yaml.Unmarshal(data, config)
	if err != nil {
		panic(err)
	}
	return *config
}
