//
//  ButtonView.swift
//  Lunch Lottery
//
//  Created by TommyVC04 on 10/17/22.
//

import SwiftUI

struct ButtonView: View {
    @Binding var isSet: Bool
    @EnvironmentObject var modelData: ModelData
    var landmarkIndex: Int
    
    var body: some View {
        if isSet {
            CancelButton(isSet: $isSet, landmarkIndex: landmarkIndex)
        }
        else {
            ConfirmButton(isSet: $isSet, landmarkIndex: landmarkIndex)
        }
    }
}

struct ButtonView_Previews: PreviewProvider {
    static var previews: some View {
        ButtonView(isSet: .constant(false), landmarkIndex: 0)
            .environmentObject(ModelData())
    }
}
