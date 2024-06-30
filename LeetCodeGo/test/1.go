package main

import (
	"sync"
)

func main() {
	m := make(map[string]*struct{ foo int })
	m["foo1"] = &struct{ foo int }{foo: 1}
	m["foo2"] = &struct{ foo int }{foo: 1}
	//m["foo2"] = 2
	//mu := sync.RWMutex{}

	var wg sync.WaitGroup
	wg.Add(2)

	go func() {
		for i := 0; i < 1000; i++ {
			//mu.Lock()
			//delete(m, "foo")
			m["foo1"].foo++
			//mu.Unlock()
		}
		wg.Done()
	}()

	go func() {
		for i := 0; i < 1000; i++ {
			//mu.Lock()
			//delete(m, "foo")
			m["foo2"].foo++
			//mu.Unlock()
		}
		wg.Done()
	}()

	wg.Wait()
}
