def run(program):
    variables = {char: 0 for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    labels = {}
    output = []
 
    for index, line in enumerate(program):
        if ":" in line:
            label_name = line.strip().split(":")[0].strip()
            labels[label_name] = index
 
    pc = 0
    while pc < len(program):
        parts = program[pc].split()
        if not parts:
            pc += 1
            continue
 
        cmd = parts[0]
 
        if cmd.endswith(":") or cmd.endswith("::"):
            pc += 1
            continue
 
        if cmd == "MOV":
            var, val = parts[1], parts[2]
            variables[var] = variables[val] if val in variables else int(val)
            pc += 1
        elif cmd == "ADD":
            var, val = parts[1], parts[2]
            variables[var] += variables[val] if val in variables else int(val)
            pc += 1
        elif cmd == "SUB":
            var, val = parts[1], parts[2]
            variables[var] -= variables[val] if val in variables else int(val)
            pc += 1
        elif cmd == "MUL":
            var, val = parts[1], parts[2]
            variables[var] *= variables[val] if val in variables else int(val)
            pc += 1
        elif cmd == "PRINT":
            val = parts[1]
            res = variables[val] if val in variables else int(val)
            output.append(res)
            pc += 1
        elif cmd == "IF":
            v1 = variables[parts[1]] if parts[1] in variables else int(parts[1])
            op = parts[2]
            v2 = variables[parts[3]] if parts[3] in variables else int(parts[3])
            target = parts[5]
            
            condition = False
            if op == ">": condition = v1 > v2
            elif op == "<": condition = v1 < v2
            elif op == "==": condition = v1 == v2
            elif op == "!=": condition = v1 != v2
            elif op == "<=": condition = v1 <= v2
            elif op == ">=": condition = v1 >= v2
            
            if condition:
                pc = labels[target]
            else:
                pc += 1
        elif cmd == "JUMP":
            pc = labels[parts[1]]
        elif cmd == "END":
            break
        else:
            pc += 1
            
    return output