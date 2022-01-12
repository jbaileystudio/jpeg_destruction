import os
import binascii
import sys

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

script_path=get_script_path()

with open(script_path+'/edgar.jpeg', 'rb') as image_file:
    data = binascii.b2a_hex(image_file.read()," ") #inbetween every hexidecimal representation adds a space
    #data = binascii.b2a_hex(image_file.read()) #no space

print (data)
#print (hex(data[100]))
#print (data[100])

#hex to image
#import binascii
#data="FFD8FFE000104A46494600010100000100010000FFDB008400090607121312151313141616151718171A1918181818181B181A1B1A171A191A1B1A1A1F28201F1E251D181621312225292B2E2E2E1A203338332D37282E2F2B010A0A0A0505050E05050E2B1913192B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2BFFC000110800A8012C03012200021101031101FFC4001C0000010501010100000000000000000000040001020305060708FFC4003E1000010204040402080504020202030000010211000321310412415105226171328107134291A1B1D1F0065262C1E1142372F133821517B2C21643A2FFC40014010100000000000000000000000000000000FFC40014110100000000000000000000000000000000FFDA000C03010002110311003F00F31C6241CA0961742C7B075496AE5B11A870CE2039F981650655CB332868B4E9E6287DF13AA5C1AA3E5AE966BD34A87117E1543FE39954685EA826C41D95EE3D0C04244D243DC07F21A8AE9D0D37D0C5B3A6850ADAC6E483BEE41F782FBD5D182292E92EE59C7B5E5A2BF4C0F30EA3DDF4FBF85001D84C764E45F320B5EBE7D7DFEEB8B71D86E50A49B501D1493E17EA2A97D681817032D2695AA5FCC7DEDAC1783C4643915542B5BB3DE9A8DC7D2028C3E272BA4F84DC1D08FBBE94B8894E93B58860F7FF0012D71B11A5438B13C470A0574670AA9CA2CE7554BEB74BD7F50D2C532AA9A8D435DC17A8D6FD411780909CE18DCB053D891627CBDAEE7B404E522A0DB9485569F95435EFFE3B44BD493AB286BA1E87EBD082C6D10A0F955CAA14EDD08D4405A99AC73A43CB246649AE53F6ECA1D8EA20C9E8CE0F3314552B3B6A999F30BB100BBE80C9065A8ED5717EEDB86B8EDD0C6CE0658354D08F3A59AB422CCF42C0162CA20017524E64B2D0C1683AA4F855D9CB5F5491B9CBC449672976D46A9D9FCC50FCAD1B58B4196BCAA0CC0B1A9649BB3D548AD41AA4EC7C4119673B380AD0FB2A0743A3100D77F800F85C5149AD47C8EE3AFC0B748B960684655F84E8FF0094BD8F7E9BC3CDC354E50CA1741D7B0D7B455252E0E5E606E8DFB75F9C00F365D0EE9F78FD27A7DF4852D564AAC6A0EDA1AF7FBB1174F340A770CC15A86D15B8B751D75A24B1707B81F363D69E607981F270EE420D17EC1D147F29EA6DD5C0EF7053351C29F327A8F165D5C12ECEF50455E2BC04E053917E1D141C653A751FB5C6A0BF105A8165589052B1BD59DBCD88DCDC0A003C4B0ECCB41749A823AEFF0075E85C00E5249AA18287B3A2BB7D3DD1AA9ABB5FDA4E8A7D46C5FC8F5810C800B8B1A763B11A1074D58F7215495D094D98852350F43E47ED8B3C153B94257CC9F655723A8FDD3F23054B659A9CB334568746574D1FDEE2B109B25DD2A1955B68E05C797CC1A86300D2CAAC79A80FF90163D682F70CC7A5E714CC455376D52F450EC7DC450E902C859433FBAC4751B1F87B9C1332566F0D17A0140BDF28D15BA35D3A8129CB39C039668140EC1436726FB127BEE415A8A54D50B1A3116FDC6D7F94232DC029BFD823CB689999EB52CB2CB4F8661DBF2AFA599574BB1A330465EED455C69DC7D7EAC74251A1762FA9B286CAAD0F5E84B86240B21C1295021576B13BB69985F655778216BC852A0D94F76A5C117A6A2E0335818094AC384D2B92D5AAA59D8EE936F3D0D22B9A1BC258DC6CA6B149DF4DEC0F52A70CA1C785831B9483676F120D9DBA7E9214EBDA86A4037FD483563EF7EB00C4A668A72AF6F9B77D53EED8D052A482FA9A8D3FC87DB8688E265B310686A950A3F96846A3A79C15266FAC9642BC4963DC58281DC1A3F50FD007CA16039650A3F4D011A8D3DCDB43256A49C8A705354EADF9803620DDAC7CDE1941E82E28CD71D06E3F2F6220B9044D4E555149AA54350F7075AB53F77CC022494A8E5143E3469BB8E9AEE3DEDA52C2161DD3B731A8FA8EB19D8D92A480AB149671B1A8F882DE7104CD49B820EAD97F7498030AFD590ABA0EA43E5FD2A1AA6F4BD4915706A9F27D5967FED1AA4DF20559F4524D9EC5B43694A9D95D252EFE2468B0284A468A1AA7A746160640B9549362CEA964B3823DA49714B1A58B1809C95A92EE0580502E4293A17B9037BA6978B31494A8E6AB1A2C7B495684FEAB10AB2AC7AD6801242556BA4824B0DD26E51F14FCDE605660CDEB00660D96723D929D1C870D6A0D5C405489052481CC0874F523C482372C5BA84B78A2B9890A4BA6DF23B1FD8FD8B44D2EE9B021C6A36EBB31B8600D84454904E797FF0064FCC36C7F7DD9C2DC171029392638483450BCB56E3A68458D5E0FC5F0F740091472404D86A552F60E5CA09B28905925B23104167A68FB6C7A8FBD6A670CC71947D5AF990A634361A292469536A872D5808E1945AB56D46DBDAD4B368C46825C4304E9CC2A05F5296F9A479901AE2B174C43A8949E7773A099B283512B3EE276343761B10FCC9F1060B4D9DAC5B42D4F2D3D90CFC34D66CC1D9811B816F73D0FD4B9AA4FAB65209CA4F29D527F2A859EF4B280A6D0A7E0C78916AD1BDE1B7FD3AE8DE114CA98403623517041E9A82DF0D08A06BA3152E74B289B452066497B26C58DD926A0D4A524853A446362652E596B8D0816B105B714A54106848630EB980655A4B652F52E526CC4EA936CDA8A29AE2B462082523C3709AF8761AD36B8A91A880BA7CC4AD293615622A65117491ED4B04F70142F581F132C1532F957A281E55F73BECAB16DEA64A97992552CD43121DBCFBD5BAB8F21E54F7050A0E9D51AA752A47CCA7BB6B01A12CA5745B266D94F44AEAC336CA7A057563BC67E2F07954E90C354EA93A8FE3F90213096BE60CC15BA59995D40B1D81DA8A5E29540BE6160AD69A1FBA694680B64B3F7A1EA0E87EBB81B45F266F8906AC0D19E82A5B70DCDE5A168A48CC29458A83A281D3BDBA4426215CAB4B85A4E9A3569DB6D8ED00B1385E5CF2DCA05D37287F9A4D6BF22E228978A777A92194F65359FAF5DE0AC3AC95E797CAAAF28B107C4900D08E86E1B6789CEC009A9CF2832BDA97F3287AB3DD3710004D451C3F43A8237F2FB68B65CFCC02577D0F6DBE6DA3B8A16858649700FB56EFA3ED5D748B8E15EA2AF7077F2B1FB1571003A939992ABBF2ABBE87BEF6FDA7200AA163EF4FE0DC751487992DC6A40F78E8771F3F788BC202C328B101C1D9AA4F51AFBE02BC5CA55957A14AED9A9ED1FCCCDCDAB0EF14A0E635E551F2AFDF97EE74959FF008E66B63A1EA0F7F8EC5C11E74A2939541C6C2EDF991D458A7A37F883C82E0121C24D46A06B97A50D2E921C38A44DEA5248502C52AB058D1CFB2A63457BDC456998CCE457C2BA80A6660AD42816ADD259E8C614D772C1940F323E2E3DFA5DDC3124405B2679942AE50E402C1D04DD241A56AE3C26B77824CB42D2E8ADDD2347F690E6CEC08268E2BEDC0D2B1093CAA6CAA0C146A00FCAA1A80A0E0DC68C5E059B2D7254E9761421EDE62E08B2875B10440362544259DD8BA4EFB83D5C3EE083A98AB0D3C02E03BBE64EB5A1CBDFE9B45B3E7050CDA2A8A1FAB7E84DFDE34681E54907BBD1AE4F4D95F334BB38310E59DFF291A8D08D8F4F756F74A24EC5776D17A123A914235EF7AE6CA3422B9BC828FECAE916499A1432AAEF4558B8DF650DF5D77217E0B1E95032E6BE57627503AF50C0FF00D43EE079D872839487D880E08D08304627084B6660B228B66130598ECA0DF2E8E0A31535032B90DA39101A33E505070E41BBF881F65FAD28AD588BD0512672BDABD47F9A45C11B8727B13E7398BCA41163EEAEDD0B02DD0F4822514ADF455C1D0915B9B11B9DEB562A01C2D20657E47749FC87707687623917DD2DA3EA9EED6B12221325F310033BF25AD7CBD696FA434B3CA10AAA6A65AC0F0EE93D2C72E9A5EA062C959497099A699BD959D95A0277B54834A8AA6A2A4A414AC55493D2F7F8FD2B15CC596AD45330DC68A07A6FDA1E6CECEC5C922A956A08B82DEFDC694A40213D0AA2C657A13B75DDBE3FBD4A4996722EA97A6E93B83F60FCAB532BA2FE047DFDE8105B72A9C8DB51D46E3A7C8D602E59506CA7B6C77607E298B953C2C8502CA6A1DF74A9EFDCF47A540CD97949749AA555B6FBD0F982FD4169B2CF653BDE8A7B106CE77142DA180DBC3624D8F8B6362DA7C59EE28EE1C98CDB661A1653FC1FE4FD03E8A8C9C3E2949EA3516343BE846874EA291A9308CA262799079545AA35CAB02C43386D9C5290004F964D659ADABB9F64BD9ECE686C5B5A644DB3820A4B116293B574B86366DAD25823991A508B820E846A0DBCC76064B4A2726F9559684D59BD956AA4599574D1DC581D09198149F13DB5DDBAD453A8D5B341484AE879660B286BB5BEC7C201CEA964A143BA49D7420E8E0D15D7506A51505EAC5E8AB5763B2BE047BD211992D4955032F54E8B3D1B5D585EE2A2252E485074EF54F5E9F7A6F426E117EB3FB73032C5053C55A86F9A6EE5C56859586AB1D4514FE206C49B13B2B5D6AEE02996CDA52874DFDD7AF78B5335EA6E2EFD37EDA2B4F99B874D32CC0E1EF62FBD6CAEF42D5AD604C6E0152D4EEE93E1507D2E2B622C526A3B10484A661812169DC38FF5655ED450B6A20F90412331014FE2B025A85F424357C8B82C33F08A20B790D7C88D5276DD998C68CA4822B50CECEFCA7AEAC7DAD8976201806E25C3B355994E7A662CE41FCAB66EF42E68A39E84927F51A31A051D417B2ADD0BD58DF5138A23915CC198162EC2A0285E8FA5525C8D41A71186CF9985581D08B50B8A1046B662FA3240554AF6FAB1277D52B1BD3E1E6633B0CE3321C149A8FCA742371F7DEDC34F25D3328A6CB98D94344CCECC19570D5A545D2E51D34A106E9E9D46C7EC065CB99428507474BA77293D36E9D988421C04ACBA4F8260A547C428529DAE3291A523870592ACAC410E40395F7EC76BEA2CD0DFF8C54B2433A555CBA11A1046A2AC47D44064CCC3949214010AB8B05F5FD2B0E6A3E20F34D1860CC5CA4512A6E6403ECA86ADB6A1DB511D00E1B99205C1B3D3C8ECAD8D8FBC406AC194963D4545C6A950DBFDC060E2A490588BD7A1DEBBFDD62CC325590A54E469B8FE0588D8F471B788C1A48DDAE09F26277B00AEC0EE6838129486A8721C8A8A552A1BB5C7BBA063270AEF9439D53BFDDBCE04992B2A98541B1DC1B3F5FE63A24F0D2486A2B4EBA79C5B3B85E7E6667F10FCA753FE26FD1CECE43212D313400AC78D2681606AFB8FCD70ECA70E605C5E16CABA54728510C4285E5CC1A2B5076B3E9AEAE1A431729502E955ABB13A1EBEF8BD120CC74B04CC34525B956D661B8FCA3774D4080CEE153C94AA5283915483AD2A927722C45C848B448C949A850F301FE2A1DE2B5E1149566AA424F754A57978904BFF0006E940EA905EA2EC1EE0368EEDAE9A40533D218821C17A00C15D51F955BA2C6E368164BA58820A4D89B2BA1FCAA0F7D1EB42F0D267B86351B7D3A88792B651D525B30DFBB5957E61F510052D635760685B990747D1C7B881EE532684ADCF855570F955FB8237B8F32F29920A280BA481954DA10E90A1B7D8DA1BD530621D26E97B1DD27F7D45E01B112940D0B8DE8F5B38B56BD0F7040104B724A45754EFD47DB88D4C3CA29606A92EC5ADB86F738FE2273B87905C50E9ABF63AFCFCEE19058B117B7FBD8F5143D0C31531CAAB68751D441EAC2DDC575A7EDA83B58D2C62430B64AA83D955F2FEE53F11F020325B2E555526C47CC6C6DEFD4522450C9093549763B1D5ABD894BB1A1075827FA2523908BF98FD2A0751D762768BF098577491CA6E9D88DBEFE30010C31BEBBEEDBFD6E2C7A11832A412DA8620D8EACA1FBEFB69B982E18A16AD1C1DDBF76F8760C5CAE0F9EA8BEA3F71F4F76D018278705033248623C52CDC6E3A8672FF006074E0CA92E870A05C6841D8FDD7B8AF5A9E164553434208A31D7CA0AC370A0A5660005EA1A8AEC37E9AE9B10E266E094A482536B8DB5A7E935A69A3562238791D8D8FECAE9D45469B47A38E189F100C45F5F7EE3AFD81B13C1817CA3476FA6E9F95BB872C8C115A03865A5ABAD3C25C74D46DE50722489818B662E7400ABDAE809BEC5EB50F1B185E1C694EE3A7482CF05AF4363F23DFF980E72561DAE3A1707DCA06B4F78B41DFD0F2B0199240749D85883B8A8CC2CDA825FA11C2B3019A8A14CDBB68ADE9AFBE96A978432C8041001AEE376E901C363387652E9A8F88E87AD3B1F95427E550501D4A48D7DA67D0877162091DBACC6E1D24382CF43B79F471E4DD9B97E23802998504104B0058B1D12479DBDD017E2706159572896500C06671520393570410FBBBC6860304B98960085A2AE1DC574D8B976D5CD5EF7701E1D36BCE25AC109A9CA4850152CFCB4157D04767378649494A96A4A3FB60D06CCEE05817FB101C6AB81E6BA6BFFC85BDFF007D22B95C1082C5C8141BF63D23B73C4F0AC53989C87F215063A92058D39ADF083E526494A7DB04D1410A62ED4516D0E9BC071D23859C8135CB989058063E5B1277B968D0C3F0ECC9CAA01C7C0FDDFECC74470492AE5CAEF54820B748B860FF00DC072B88C06416EE3F6319F88C28555BA39F92BF6547678BC2834D37FBD3A467FF00E3F2B86A180E3E6600EDF7F7F7782309847497671A1B293A83AD2E0DC5768E8FFA06D3CA2E4F0CB14DF4EBD0C0730AE1A0545506E0DD27CBE7623CC45FFD2EF7D15BECFD63A2958163F76D8EE3FDC11FF8C0D6A7BDBEA3AC072B3387050B575EBB1FBFE2039BC1C2981B8F0ABE201234D8E9DA91D92B86652C6DBEDD62B9982228440728BE199BC439AD9A9CC3AE99ADD15F1808F032E59C767BF67A768EE2560FA38F97F10EAE1BB379FF001780F0DFE88BF2DDFE3B11A1E9AE9B41987E16561D22A2E9E8751B8D1A3A35F0ECCC4F8DBC5F9FA2BAF5EEFD089720063635F23A83F3F380E6E4E194000CE038AD8A4DD3DAE7A131A183C0A4A6BE1DF542B47F7DF573631BAA922651805ED60BEDB2BE07E71C2C8282694B5BE041F7107780170DC2D8B287D0FF003F7D09E387248C8AF0DC11749FDC748D0C1A41EDB7E5ECF71FE8E8609992198B53EEDF7FB180E7311C2458B3E87450FA5C4569E13A11F7A281F87CE3A8187068CE9356D8F4DBB45A9C238036F09E9A8F2A16EFD203024F0D4E5CAA0E2A435C1D72FCCA6C74884CE1412411EF11D4230469D3EFDD171C0EAC2B56D3B4073F8392DF3F77DBC1870801CC9A3FC0EA0FDB46BCAE1A1DC0EE351D7AC5FF00D0B1E9F7F0FF007019899414F463A8D7B8FBEFBC3A302417F711AF6FA46C2705E4DAC15224369DC6FD46C6032448763ED6FBFDFDD6B17CBC1EA2E2BDBB7D3BF63A8AC2867151F7F1864CBD7E3F580CC1800F40DF2F2FA45A9C2E84563404AFF5F48B9325EF7DE033861C6D0363E40296DADD3F88DB18781F158580E166CAF18651524166AB00E4F2EDF2AC552F87A1600567012AE4989674BDE5A0317035D9DC47498F9289685CC5000A45F6607F81E5AC728710B0B52C9D58378549A9AED992087D481524406C620A42C098D94A8299142AA3D540541652A837EA0D13501795A6139D553CAC8B657028E0333B97AE860544E0BCC9E6C9476F166704943D8A9AD6094E8E22CE1385609284FAD0A5A88FC8905C82926CD407AEC1301A586E160489D2C150984AFF00BA5456332B9B3657B104123AD6F5E778771D5265B310B42AC9648E5046796D5007353C43B384EBF14E225129594FF70A921201CA729A950A0BB9602FA465E270A7D592AE696005656658372A041151D2B0148E33CC549202D5E32FCC876292456875D6BEFE8F81FE2850012A49989FCCEEA4821EA75172E6B1CBE27032D4A4CD94900A92EE4A815EEC3300E0E84D7E79FC5B1AA90A4AA5ABFB6A014C1D8117B8F783580F5F9188973539E5971AE841ED789FAA71F7F08F25E1FC696851992C90A4B9649D9E8524B2924B38BD7DFEA9F87B8AA317284D4B3D9491A1DD8E847DD202E4E1DE9EEEB0F2A4376D441BEAE26110032A46BF1FAC24CAFBDA0D423DDA886F54DDA003C82C453E5115486B871069970E13A180CF1856A8B44C49FBAC1B91A1FD50301E5B2F04FA771B751F7F0B5C9E18E18F91FD8F6DFF0068DC93846EDA182048D44073B2F865588AE9B83D3E9054BC1B9E6BB5F450EBDB437168DD4C80AEFF0076FA7BA2CFE9F71F7BC062C9E1F96A348D24618286C751D77106270F134C880CF181682A5E1BEFEFEFE307A10F7BC5824E87C8C0028C3318BD586DBEFB7D20908D0C5884E9A4004891167A97D20BF57F1D625920044C989FA9828262411003A659FBD7F98464ED05E58904C00424C5889504E4841101584FFB84A92F1784C4C260387F4833152F0C93954419894929A90925CD3534E958F38E298A3949D02959546B952D980A5C555DC28D892FEE3C6B84A313226485961312CFB1BA4F91023C678C0F573152662322C12082CCB605D9218552AA0D74BBC05BC1F128589652A629CB63B82D99F42901247431B782284A58A9906A901C312E69BB92E03B54E8638AC4481298CA0721527C20E649140086B6525BBBEEC1A31D3D09295228C12EACA43B240A176729B3D2F01E8BF8F31386FE9A54D1FDC52CB029009197C46977B3ECDAB18C9E1BC4BD621981245147C25E84289D77FF00FA6353849E26B9D8528094F885569E74281AB124317A3D7A80EE69E113885E498082ED99258B8D4FEAEB63AD2037F178521F28398A0A58174916D6C41D6E35DC63E1E4A59289E853537D1EC7D92017E9D8C68A788A9D4145EE5245086BEAE15FA4B91A38A451366129CB9F302CA0A480E2BB0AB39B0B7680C4C4F0D12541495BCB7E5526E950F65690EDF6DB46E7E12FC41FD36225E6294A545A63552A411E207562EAA6CA035002E292952DA6A00525B2CC4166983A80685BE4922C4463E1D4851CA410824948533A2B421468E3AD0EADE201F49897471F7D61CCB8E6BD1B63D4BC2A64CC566992004E6AF320F81DEAE072907F283A88EB19A0294A61F2FF00A8B08D619A02A288668B9A226020CD09A240C2CBB407342544D0968B8235896480A0C9F74132C3DEFBFDFDFCE1213124A18C03FAB898445894C5899701484C5A22595BB43E5808B7BBE50F962403DAFB4278074C488883C4D27DFF00380748890861124C0381121092224D00CD0ED0E06912101110E21DA11100F9291CE7E2AFC23231A015954B9890C9992F2E602E01CC08207BC39621CBF47A3C56B98901C90040798E2FD19E23324CBC70CA971CD28835DF2A989EB4B0D83727F8DB82E2B86CF938824CE929992959C0E57411CAA497C8FDCBBDDEFEE98CC4225A732C803E27A01AC568289897490B4171B83A1101E35F8AA584F11C4B007D6144C4BEA14840269A3BFD22BC070A44F0AF561D72DD453AA93AD7DA6AF5A46F7A5FE0EA96656390F95004B9ADEC824FAB536CEA293DD1B470B85C629273C95E49832B653722AFB3100F979B06895B1E64BA4109ECC68FD3ADC5AD01A271CE5252D5201018824BB2B476D6C69DE373092862254C9EC0A802272038A13FF227A0D754F6B0DFD3A487CCA009487D4507885AB5FB2F00349466052C450A487F71236E9711949904266208E64B2D2FFE40114357A90450B1D6FB6C25AD80198A85459413422B621FCA8F17F18C289B284C96067964129FCC851A96DB71D202EFC15F88C61B152BD61FEDCC09413F94289480ADD295807A7331B88F7031F31F14C22664B9794E5528AD2097634472A8F73DEA2F48FA33F0F620CCC2C85939B34A9649B39CA1CB685DE900744624622440230C61C1862202B221A2C86220381C3FA42E1ABAA573496516C95A073427A1A41327F1D70E2952B3CC0120A88C84900162A60E59C1F9F58F9F4F3541E615EEDA8EA2BDABDC5895970DCAA7A292CEFD0FCD3AF7B87BEA7D2070D354AA6AA84FFC6A0E033B38A90E1C0AC3ABD2370D6A19CA2012C1049000727B50D7A6F1E1326AE0D08D1363FA92DA74151A7E585EBE66600A885A6A8342140D8A7473F96CAE86E1EEF85F499C3169CC153477966CECFD81D7463A082D3E91B86B039A6788A7C1621AFB0AB8362013611F3BCC95983A5810E5AAC7767D3706A1ABBC11809A486A86EF423F30DAA6BA3E8F01EF33FD2670D0A29CD31C202CB21C653F7F3DA2B99E92787A5256F30A416A4B275DECD1E1B8996A282905432D7287B39761AA5CBB685DAE4404A5A880A0A658B87BFD46E3EA583DEA4FA47C0AC808F5A4D9B255D9D8B9F8F43B16BA5FE3FC12C900CC0A01D948CAEE010398DCD81B121AF7F019335DD40E5551D9D8DAE350EDD4696A5D3144F3064CCB10C194FF0002083E1B1AB54310F75C37A40C1ADFFE5194B10A9642AEC592798B1A1A521A57A4BE1CF9734DB0FF00F59DC241EA1C8B3EF68F0F388330E70A289A906A14A703A9BA91D6E9B171503CD99EB0907917729AB3D4F28DAA4E5EBCBB407D032FD23601D8AA63B288E4B80FB1B962C2E7DED295E9338712D9A60AA535481555A8EEC77B6F1E032F10ABBE6A552FD01CC8EE002DAE53B02095CD2A0996B565748F56A2480524060E6CE000F47143B90F7A57A42C131534E601C9F56A6FF7D2F434A40E9F49B822ACAD35FF00C457C5A139BD926D6BB4783E4C4CB5E45217703290A0096B3117A79B6F04C8E0D36657D5CD29572BE45F29A312E2D667BD8DDC87B6E2BD2960258E6F5946F65EEC5D8176AED0FF00FB4F87E570661724304B56BBDAD47BD378F26E1BF81F88E29BD5C850605266299090406A15B664281046572924E948D4E1DE8838A850257224E959A4901AB440218B017DA03D0FFF0068E0A949811CBCC50A74E66CB992CE017A1663A5691A1C23F1FE0E7CD12904B926A580601C9A976761DC8D2B1E6785F45D3E5CC266E3F0684B10EE66155B95485048208B97DA85811B7C3FF0570EC3AD53667112A2016C8903D5BE5CE733A896367A8043BD0C07AC4FE2B2514CC1C36A35B450AE3120A49CE92DD44790F12E11C3264C514E2F1CA53976426A41485556122AE0B6E5C75D1E03C77058074E1706B2A58FF926AC15AD22808512AE5A592C01D1E03B09D8BC14E992D39815924A12146B43B1AEA7CBA4118AC3FAA01280B4667F092D5DCD5BBC71123F1F7AA4FF00670B87908531A10D5241242529A38A1D6B62233F8AFA43C58492664963401282E2C7989510C43B1ED01DA09989015254113A4A92A044F2EE086CB98548AEA0F969E6B37D17F104A8AA49C3E5CC72A7D6A814A497039D3A503B97A6A1E127F186226056698B580D601C59C365A281AEC41319F378A28AFD6133140E60005280EA0A5CD5890DD9A035E77E17E278349989082BB94CA98144A43E61A1FD40876E604581CB4714992D7CE92C487147735B0A02C4D050D48D40C3C2712595039405240B29AC900115A822FBB9357262B5E2C098480965001401706B4F37FE18DC3D0B0D830A280A4D094D35E601943AB11E4C0F4D23C20E15E7104A00CB404BD2829ABB8F38B7F097E1E463B87226A262D1387AC4A160F854952825C06E80EA77B473182FC658B965586C4225A969252A4AD2A05D3A28666DAA035B704853C30CB4CF4C9C40FED4C0B4B785C29828D1F2FB2A6D0A41154D3B8F4378FF00ED62706561670F39450A06AA42D4A72DFE69512D4756F7C45F09C3E3657AD94C99C8490B976CB62E91AA5C77049EF193F84B14B91C4B0EA01D6A57A99B5A4C42D9215FE6084ABAE5A07B87BA1111789188BC0448861127862201110CE61C1896580F92D58122AFE120E61623D93FB3DC3B1E9132B33F2B176506A13B86D6BA6FD6BE8586F46BC401659C34B4A99C19AC52E2A3280A07B0E9783713E8E46503FACC185814012A7490428B2B3B9A06A8B13B9243CC960D15B9AFF9369D48AEC7DD04A66021A624901C90D50F7525F7D526EE0D090A3DCABF09E012E99F8D04900912B0EB513A96274A3802CCA2EC5422E3C13844B292A9B8859294FE496163D87535096BDE9A3080F3C52882124B93542C12D3077D16373D42AD1054D2EE0E5989A03BF420FCBF68F4B57E21E0F2A5AA5A70095142DCA66AB30CC6E4BB86BD2CCCDD25FF00B190803D46024208B112D2C1360A76491F7580E0B856127623FE292B5907C32D0B51412189040232D4063A11A5635E4FE00E205455FD1CCE4582F6CD94D192A20977AD34DADBCBF49D8F0A23D5CB4820919400096BBD7DDB450AF4853D61695CF9A144009C8120E614720581A1A1DC4063A7F03713480A4E014998FCDCE965825E83372529EFAB9683785FA39C72828AC489403B271135398977CCC9CC1989BEDE70362F8BCF9A1B3E21448203999E1342C0BD6F6B351EC736699657FDC40CE004A94B98415A4BDED5620B9BDCEB01D9CBFC03204A2B9FC424A16939BFB492B0920101D4A57333D0B0F386C460BF0FFAA295CF99316A2E264A0505212524A50909CA016AB8375335871985C5E570C821F2B0CC42A99559E86E1FCCEB511004864A7940774894C527F324D3BEB4DE03D47FFCAB84A512D28C0A5791FD5E7972731CACEAA97CD472E1E862C57A5994A5002400B144E76AE8329029F01EF11E63873EB014A94C6AE4CB2C5EE54C77ABD680BEE29C4E1327B2DD0E9BD0B37672E0822E203D0311E9866952A5832905C84A8A56424DB9C1340EE1C5B949152C2623D27E33D61499AA4914C99515A063999DF5D8BECD1E649419A765806BA102EFD3ADC51E96D74A148190B86A24EA01A80F57497B77EA0875F37F1D63684CD5A82810090AA11562120007335ED6B5630F1DF88B1330013066ABA7D614BBB105B31D41B10C6B022710FCA48702AEACC081A904B11D5A9AD2D4E230E40130A031E95A3FE934A163DF468069BC7A627214A8650E002EB286200B8CAEC059EDA520C1C4A79198AD6412EA094E5215565024E50A67AD41AE8633A7C9F5A03D1556248A83EC91CA05855ABF2225B246557620914E8439714F26D2E02F9F316919C296CEF9B304DD87FD48D45C3B82C43052F1005C150DF39CD5A1B0BFC0B07AB11A7270E52010391418D0B1D1890056AC1577228FCA40C4610A1448720BEA36B11CD70D01690416A335193CAA4DE99CD2F54F5D8C15819A96292F908B5393650CA1F2BE97009B83156111959851ECEA046AE3C36AB1D2BB9106CFC027324A482ECCA05357D090EC6874AB38AD202AC4E0948214902B67248EA92330714206E0D2045E0C159286E720B339D5806770E4876A53CF770B8801265CC2A0362154BB96E471BA770E2B03711E1C99AF915917749041A937B925243F9B3EAC19D8794950001E7150494876A8BB035F2DE30BF1228A67666625C9A258BB1B025AF6EB1D6E170D9424365581CCD9F2D0315039431E8FFC60FE209A97099842C3B05B2A819F29A9A8714B8770E0B10F62F4198A0BE1CA03D99CB046CE941BDCDF5AF7B9EBB8BFE1CC2624E69F225CC50F688650FF00B0657C6386F40F2C270988482FFDF0AF232D0DD0DAE23D31E039095E8E30299A2634C20050082BE5A86BB672CF475529B08827D1A603366509CA0E0E554D53020822A96569A931D90868084B400909AD03072496EA4D49EA61CC3C3403434398680509A1C433C07CCD8DC74F510A2520DD0B2A7714B6ADD2E2BDA2995C516525216028B1243BB8B17B33EAD4688FAB49700023C451BEEA416A1FE6FA39C3D3385129DDEA3B87A114E85FCE01CE2574CCA59A977A39DA8031FBD989C6E0A5E51CB9904387554663D1F5046C48D0981D52EA09009ECE08F75ACE2E3B346860544A4A124020929CD563ED214E6A14198B5D207B5002E0B1C9E513084AC0644C092AE5A0C8A259ECE0E9115E0F3120959580EC08CA46A410E68E29B1F28AF1586079D22A3C49D527A30B6B7A3F99BA5673C994AD394A9EBCA054977A01F0F84066CE4650A70FAD7353721FA6C0C48CC5E50A05A83C2F5EEC20E2942FC4D99D9DC07DB330A1BF7EEEF5AA52924050BB8008241D0F8942A2BE7014B929054E7B87DDAAA3D4F63DE0B9C153415124CC000AA915000096CA0D43247BA28C1F2929092A0A2C534BE80302733FDE904CF926597A94B905F32483AA16299543F91D00196555CC0DB799F41EF82242036558603C2B6729FF002E67297F31A6B0A7942EED986E0730A753CDAF50F147AB228136B728D7FEB01A72B87A926C9075609650DC73546BD58D8D22666D04A568F94F3729D1347050A0E370588B561C331447F6D7507C3CAF955FA5D3AD8A4D0D2C624A96951144B1A8504B36C430B0D754BED500209405072ACB0049143A1D2FBFD08164B98164050658A3802A9B1615B17396FE2EC14C536C92E411D487760CE0804B6EF76A3FAC25EAEEC480546F6524825C1A575A03A180A965614C429C6E48DAC4338208208FE609072D699280DA8F62C547A166AD46A444A62D131002C8CE2895900661B28AAA0834A9DABA9125A952C90C68E1ABA5D2454540B6ADEE053F0E12A2C282A00D0588709A80D7EC62FF00EA9F2A55D085151B067079853ADC7681264D05A64BB6A0DC757B91A3DC307B3C5985C666A06777CA0DCB3B8E6BEBEFD1C00370F88605241503D1258D8B78AE9A1162C2E20D9452AE57BB805C9F22091F50E2A432A32C4A530080A582680024EE52D94971FB3EB04216841573A4819478E849AB976208E6A8482157EA0D36499649A31D4B020B5C38BD287BF61689E32D1C817049A8D48626A1BE5B08B158D9374CC494D9EE4167639402E48A0D74A8200CAC5C94B2C2CA8120948964E6CAA19B22D441CC017617A5600E0B2405275465528E4248A2413998B8E514AD1E2AC2F115D41767A9E67490E3405AF5F2EC6DE0065E2B112244ACC94CE0415AAA97095A949C8F71945091424D4313E852FD16C92ACCAC42CF642410CECC493514B82295101C14C9B98B29490142B415D9409624EADAB11A46671352485CB9A5AAF2CDD0A15252A02BA8652598A9F5AFAFE17D1AE0517F5AB724B2A6307376C8137A53A4747C2B8361F0E929952D2906F751346A9539FF00701E79E80943D4E2824929F592CB11549295387D6C3E80C7A8987CA05A90C4C0343FCE22F0F009E13C2311300F0A1B34454B03580778903102613C07CC93A5E5635522AC52D99049BB9AD4EFA862C62495292A7A3915BE5989ECC03B7BBA3B434280B4A12CE9728D8D4A0EC6A69B1B8F782964A4852494AC36D5A50E82BB58E95850A01C730CC917A901C949ADAEE877A5D2E748A15434040AEC1C6BB31D76F94285015CC05C39A1A39AD350A0F76F93BEA2C44EAE5582CCC6E140DBA740FF00C328500B1618BA09297E55307ECABF37D3C85E388AE6154D2B0A2FCE898EACFB9B00D405DC104F9C28500262A50354394FE5BA803A5FBF7AB55D20592A6292C14C680804137A86AB83F3DA14280365ADC005370ECC1F6CC397BC1582E138A5974C89AA04BE644B531356344D1437F7B83550A037257E08E2135DF0EA4120D4B25CD19401506A876EA5A0C93E8C3882C02AF552D4198AA6394BF8BC282F5D2C42B421CA8501A89F44739442978A421440CE10852813B87525BFDE91B186F45387A7AC9F356D4A042411B5412DA8AB8D08148785007E0FD1970E97696B5549AAC8A9041F065D0C09F8E3F0C60E470F9C64C89685A7214A99CA55EB054125C788DB73BC34280F1938F295ACD466242824B0AB8228CCF566A1B5C318AB0E329287524DC51EB7B6B6234240235014280CDC1CC507218B508350A4EC46DF7A53530612B4A86998509A826B7FFEDFBB9868501D0FA39414714C355B3296FB2C89732E1A8AA3BD1D8D8B83F4123E10F0A02461A1E140278630A1403343428500E62261428067DE0270A7EE7E10F0A02F945C758B40850A03FFD9"
#data=data.strip()
#data=data.replace(' ', '')
#data=data.replace('\n', '')
#data = binascii.a2b_hex(data)
#with open('image.jpg', 'wb') as image_file:
#    image_file.write(data)